.. _layers.layerupload:

Uploading a layer
=================

GeoNode allows you to upload layers.  The supported formats are shapefile, KML, and GeoTiff.  Once the layers are uploaded, they will be available to other users in GeoNode.


#. Click the :guilabel:`Layers` link on the top toolbar. This will bring up the Layers menu.

   .. figure:: img/en_toolbar.png

      *Main toolbar for GeoNode*

   .. figure:: img/en_layers.png

      *Layers menu*

#. Click :guilabel:`Upload Layers` in the Layers toolbar. This will bring up the upload form

   .. figure:: img/en_layerstoolbar.png

      *Layers toolbar*

   .. figure:: img/en_uploadform.png

      *Upload Layers form*

#. Either browse to the files to be uploaded or drag and drop them in the browser.  Note that many files consist of multiple files to be complete.  If you are uploading a shapefile, then you need to include the .dbf, .prj, .shp, and .shx files.

#. Click on the :guilabel:`Browse...` button. This will bring up a local file dialog. Navigate to your data folder and select all of the four files composing the geospatial layer.  Note that some data formats consist of multiple files.  If you are uploading a shapefile, then you need to include the .dbf, .prj, .shp, and .shx files.  Alternatively you could drag and drop the four files in the :guilabel:`Drop files here` area.  The upload form should appear like this now:

   .. figure:: img/en_uploadformfilled.png

      *Files ready for upload*

#. GeoNode has the ability to restrict who can view, edit, and manage layers. On the right side of the page, under :guilabel:`Who can view and download this data?`, select :guilabel:`Any registered user`. This will ensure that anonymous view access is disabled.

#. In the same area, under :guilabel:`Who can edit this data?`, select the :guilabel:`Only the following users or groups` option and type your username. This will ensure that only you are able to edit the data in the layer.

   .. figure:: img/en_uploadpermissions.png

      *Permissions for new layer*

#. If no destination is selected, the files will be imported into the default spatial data store for GeoNode.  This will always be the destination for raster data.  If you have vector data that you want to be versioned, then check the box for 'Import to GeoGit'.  The form will update to provide a dropdown menu for existing GeoGit repositories.  To use an existing repository as the destination, select it in the dropdown. In order to import the data into a new GeoGit repository: 1. type the name of the repository and 2. select that name in the dropdown so it appears in the field.

   .. figure:: img/en_importgeogit.png

#. Click :guilabel:`Upload` to upload the data and create a layer. A dialog will display showing the progress of the upload.

   .. figure:: img/en_uploading.png

      *Upload in progress*

#. Your layer has been uploaded to GeoNode. Now you will be able to access to the its info page (clicking on the :guilabel:`Layer Info` button), access to its metadata edit form (clicking on the :guilabel:`Edit Metadata` button) or to manage the styles for it (clicking on the :guilabel:`Manage Styles` button).

   .. figure:: img/en_afterupload.png

