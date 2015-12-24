from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.utils import trailing_slash
from tastypie.bundle import Bundle
from tastypie.resources import Resource
from django.conf.urls import url
from django.views.static import serve
from django.utils.encoding import smart_str
from django.http import HttpResponse
from httplib import NOT_ACCEPTABLE
from tastypie import fields
import helpers
import os
import hashlib


class FileItem(object):
    name = ''


class FileItemResource(Resource):
    name = fields.CharField(attribute='name')

    class Meta:
        resource_name = 'fileservice'
        object_class = FileItem
        fields = ['name']
        include_resource_uri = False
        allowed_methods = ['get', 'post', 'put']
        list_allowed_methods = ['post']
        always_return_data = True
        authentication = BasicAuthentication()
        authorization = Authorization()

    def determine_format(self, request):
        return 'application/json'

    @staticmethod
    def get_file_items():
        file_names = helpers.get_fileservice_files()
        file_items = []
        for name in file_names:
            file_item = FileItem()
            file_item.name = name
            file_items.append(file_item)
        return file_items

    @staticmethod
    def get_file_item(kwargs):
        if 'name' in kwargs:
            return FileItemResource.get_file_by_name(kwargs['name'])
        elif 'pk' in kwargs:
            return FileItemResource.get_file_items()[int(kwargs['pk'])]
        return None

    @staticmethod
    def get_file_by_name(name):
        file_items = FileItemResource.get_file_items()
        for file_item in file_items:
            if file_item.name == helpers.u_to_str(name):
                return file_item

    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)
            return data

        return super(Resource, self).deserialize(request, data, format)

    def detail_uri_kwargs(self, bundle_or_obj):
        if isinstance(bundle_or_obj, Bundle):
            return {'name': bundle_or_obj.obj.name}
        else:
            return {'name': bundle_or_obj.name}

    def get_object_list(self, request):
        # inner get of object list... this is where you'll need to
        # fetch the data from what ever data source
        return FileItemResource.get_file_items()

    def obj_get_list(self, request=None, **kwargs):
        # outer get of object list... this calls get_object_list and
        # could be a point at which additional filtering may be applied
        return self.get_object_list(request)

    def obj_get(self, request=None, **kwargs):
        # get one object from data source
        file_item = FileItemResource.get_file_item(kwargs)
        # if not file_item: raise NotFound("Object not found")
        return file_item

    def obj_create(self, bundle, request=None, **kwargs):
        # create a new File
        bundle.obj = FileItem()
        # full_hydrate does the heavy lifting mapping the
        # POST-ed payload key/values to object attribute/values
        bundle = self.full_hydrate(bundle)
        filename_name, file_extension = os.path.splitext(bundle.data[u'file'].name)

        # -- only allow uploading of files of types specified in FILESERVICE_CONFIG.types_allowed
        types_allowed = helpers.get_fileservice_whitelist()
        if '*' not in types_allowed and file_extension not in types_allowed:
            return HttpResponse(status=NOT_ACCEPTABLE, content='file type is not whitelisted in FILESERVICE_CONFIG.types_allowed')

        file_data = bundle.data[u'file'].read()
        # TODO: support optional unique name generation from sha1 and uuid.
        #file_sha1 = hashlib.sha1(file_data).hexdigest() # is file_data only the bytes without filename etc?
        #if file_extension:
        #    filename_name = '{}{}'.format(file_sha1, file_extension)
        #else:
        #    filename_name = file_sha1
        bundle.obj.name = bundle.data[u'file'].name
        with open(helpers.get_filename_absolute(bundle.data[u'file'].name), 'wb+') as destination_file:
            destination_file.write(file_data)

        # remove the file object passed in so that the response is more concise about what this file will be referred to
        bundle.data.pop(u'file', None)
        return bundle

    def prepend_urls(self):
        """ Add the following array of urls to the resource base urls """
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/download%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('download'), name="api_fileitem_download"),
            url(r"^(?P<resource_name>%s)/(?P<name>[\w\d_.-]+)/download%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('download'), name="api_fileitem_download"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/view%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('view'), name="api_fileitem_view"),
            url(r"^(?P<resource_name>%s)/(?P<name>[\w\d_.-]+)/view%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('view'), name="api_fileitem_view"),
            url(r"^(?P<resource_name>%s)/(?P<name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail_name"),
            url(r"^(?P<resource_name>%s)/(?P<id>[\d]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

    def download(self, request, **kwargs):
        # method check to avoid bad requests
        self.method_check(request, allowed=['get'])

        response = None
        file_item = FileItemResource.get_file_item(kwargs)
        if file_item:
            filename_absolute = helpers.get_filename_absolute(file_item.name)
            if os.path.isfile(filename_absolute):
                response = serve(request, os.path.basename(filename_absolute), os.path.dirname(filename_absolute))
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(filename_absolute))

        if not response:
            response = self.create_response(request, {'status': 'filename not specified'})

        return response

    def view(self, request, **kwargs):
        '''
        allow a file to be viewed as opposed to download. This is particularly needed when a video file is stored
        in the fileservice and user wants to be able to use a view the video as opposed to having to download it
        first. It passes the serving of the file to nginx/apache which will return all the proper headers allowing,
        say, html5's video viewer's 'seek' indicator/knob to work. Otherwise the video is only played sequentially

        Note that nginx/apache need to be configured accordingly. nginx for example:
        location /var/lib/geoserver_data/file-service-store/ {
           # forces requests to be authorized
           internal;
           alias   /var/lib/geoserver_data/file-service-store/;
        }

        for apache, need to install xsendfile module, enable it, set the path and then
        XSendFile on
        XSendFilePath /var/lib/geoserver_data/file-service-store

        example use:
        http://<ip>/api/v1/fileservice/med.mp4/view/
        '''
        response = None
        # method check to avoid bad requests
        self.method_check(request, allowed=['get'])
        file_item = FileItemResource.get_file_item(kwargs)
        if file_item:
            # set content_type to '' so that content_type from nginx/apache is returned
            response = HttpResponse(content_type='')
            # needed for apache, re-test for nginx as nginx needed content_type='' but apache doesn't like that
            del response['content-type']
            file_with_route = smart_str('{}{}'.format(helpers.get_fileservice_dir(), file_item.name))
            # apache header
            response['X-Sendfile'] = file_with_route
            # nginx header
            response['X-Accel-Redirect'] = file_with_route

        if not response:
            response = self.create_response(request, {'status': 'filename not specified'})

        return response

