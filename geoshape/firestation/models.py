import datetime
import json
import requests
import sys
import us

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.transaction import rollback
from django.db.utils import IntegrityError


class FireCaresBase(models.Model):
    """
    Provides common attributes/methods to FireCares models.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class USGSStructureData(models.Model):
    """
    Models structure data from the USGS National Map.

    Schema from: http://services.nationalmap.gov/arcgis/rest/services/structures/MapServer/1?f=json
    """
    DATA_SECURITY_CHOICES = [(0, 'Unknown'),
                             (1, 'Top Secret'),
                             (2, 'Secret'),
                             (3, 'Confidential'),
                             (4, 'Restricted'),
                             (5, 'Unclassified'),
                             (6, 'Sensitive')]

    DISTRIBUTION_POLICY_CHOICES = [('A1', 'Emergency Service Provider - Internal Use Only'),
                                   ('A2', 'Emergency Service Provider - Bitmap Display Via Web'),
                                   ('A3', 'Emergency Service Provider - Free Distribution to Third Parties'),
                                   ('A4', 'Emergency Service Provider - Free Distribution to Third Parties Via'
                                          ' Internet'),
                                   ('B1', 'Government Agencies or Their Delegated Agents - Internal Use Only'),
                                   ('B2', 'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'),
                                   ('B3', 'Government Agencies or Their Delegated Agents - Free Distribution to Third'
                                          ' Parties'),
                                   ('B4', 'Government Agencies or Their Delegated Agents - Free Distribution to Third'
                                          ' Parties Via Internet'),
                                   ('C1', 'Other Public or Educational Institutions - Internal Use Only'),
                                   ('C2', 'Other Public or Educational Institutions - Bitmap Display Via Web'),
                                   ('C3', 'Other Public or Educational Institutions - Free Distribution to Third'
                                          ' Parties'),
                                   ('C4', 'Other Public or Educational Institutions - Free Distribution to Third'
                                          ' Parties Via Internet'),
                                   ('D1', 'Data Contributors - Internal Use Only'), ('D2', 'Data Contributors - '
                                                                                           'Bitmap Display Via Web'),
                                   ('D3', 'Data Contributors - Free Distribution to Third Parties'),
                                   ('D4', 'Data Contributors - Free Distribution to Third Parties Via Internet'),
                                   ('E1', 'Public Domain - Internal Use Only'), ('E2', 'Public Domain - Bitmap'
                                                                                       ' Display Via Web'),
                                   ('E3', 'Public Domain - Free Distribution to Third Parties'),
                                   ('E4', 'Public Domain - Free Distribution to Third Parties Via Internet')]

    FCODE_CHOICES = [(81000, 'Transportation Facility'),
                     (81006, 'Airport Terminal'),
                     (81008, 'Air Support / Maintenance Facility'),
                     (81010, 'Air Traffic Control Center / Command Center'),
                     (81011, 'Boat Ramp / Dock'),
                     (81012, 'Bridge'),
                     (81014, 'Bridge:  Light Rail / Subway'),
                     (81016, 'Bridge:  Railroad'),
                     (81018, 'Bridge:  Road'),
                     (81020, 'Border Crossing / Port of Entry'),
                     (81022, 'Bus Station / Dispatch Facility'),
                     (81024, 'Ferry Terminal / Dispatch Facility'),
                     (81025, 'Harbor / Marina'),
                     (81026, 'Helipad / Heliport / Helispot'),
                     (81028, 'Launch Facility'),
                     (81030, 'Launch Pad'),
                     (81032, 'Light Rail Power Substation'),
                     (81034, 'Light Rail Station'),
                     (81036, 'Park and Ride / Commuter Lot'),
                     (81038, 'Parking Lot Structure / Garage'),
                     (81040, 'Pier / Wharf / Quay / Mole'),
                     (81042, 'Port Facility'),
                     (81044, 'Port Facility: Commercial Port'),
                     (81046, 'Port Facility: Crane'),
                     (81048, 'Port Facility: Maintenance and Fuel Facility'),
                     (81050, 'Port Facility: Modal Transfer Facility'),
                     (81052, 'Port Facility: Passenger Terminal'),
                     (81054, 'Port Facility: Warehouse Storage / Container Yard'),
                     (81056, 'Railroad Facility'),
                     (81058, 'Railroad Command / Control Facility'),
                     (81060, 'Railroad Freight Loading Facility'),
                     (81062, 'Railroad Maintenance / Fuel Facility'),
                     (81064, 'Railroad Roundhouse / Turntable'),
                     (81066, 'Railroad Station'),
                     (81068, 'Railroad Yard'),
                     (81070, 'Rest Stop / Roadside Park'),
                     (81072, 'Seaplane Anchorage / Base'),
                     (81073, 'Snowshed'),
                     (81074, 'Subway Station'),
                     (81076, 'Toll Booth / Plaza'),
                     (81078, 'Truck Stop'),
                     (81080, 'Tunnel'),
                     (81082, 'Tunnel:  Light Rail / Subway'),
                     (81084, 'Tunnel:  Road'),
                     (81086, 'Tunnel:  Railroad'),
                     (81088, 'Weigh Station / Inspection Station')]

    ISLANDMARK_CHOICES = [(1, 'Yes'),
                          (2, 'No'),
                          (0, 'Unknown')]

    POINTLOCATIONTYPE_CHOICES = [(0, 'Unknown'),
                                 (1, 'Centroid'),
                                 (2, 'Egress or Entrance'),
                                 (3, 'Turn-off location'),
                                 (4, 'Approximate')]

    ADMINTYPE_CHOICES = [(0, 'Unknown'),
                         (1, 'Federal'),
                         (2, 'Tribal'),
                         (3, 'State'),
                         (4, 'Regional'),
                         (5, 'County'),
                         (6, 'Municipal'),
                         (7, 'Private')]

    objectid = models.IntegerField(unique=True, null=True, blank=True)
    permanent_identifier = models.CharField(max_length=40, null=True, blank=True)
    source_featureid = models.CharField(max_length=40, null=True, blank=True)
    source_datasetid = models.CharField(max_length=40, null=True, blank=True)
    source_datadesc = models.CharField(max_length=100, null=True, blank=True)
    source_originator = models.CharField(max_length=130, null=True, blank=True)
    data_security = models.IntegerField(blank=True, null=True, choices=DATA_SECURITY_CHOICES)
    distribution_policy = models.CharField(max_length=4, choices=DISTRIBUTION_POLICY_CHOICES, null=True, blank=True)
    loaddate = models.DateTimeField(null=True, blank=True)
    ftype = models.CharField(blank=True, null=True, max_length=50)
    fcode = models.IntegerField(blank=True, null=True, choices=FCODE_CHOICES)
    name = models.CharField(max_length=100, null=True, blank=True)
    islandmark = models.IntegerField(null=True, blank=True, choices=ISLANDMARK_CHOICES, verbose_name='Landmark')
    pointlocationtype = models.IntegerField(null=True, blank=True, choices=POINTLOCATIONTYPE_CHOICES,
                                            verbose_name='Point Type')
    admintype = models.IntegerField(null=True, blank=True, choices=ADMINTYPE_CHOICES)
    addressbuildingname = models.CharField(max_length=60, null=True, blank=True, verbose_name='Building Name')
    address = models.CharField(max_length=75, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    gnis_id = models.CharField(max_length=10, null=True, blank=True)
    foot_id = models.CharField(max_length=40, null=True, blank=True)
    complex_id = models.CharField(max_length=40, null=True, blank=True)
    globalid = models.CharField(max_length=38, null=True, blank=True)
    geom = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return u'{state}, {city}, {name}'.format(name=self.name, state=self.state, city=self.city)

    def full_address(self):
        return u'{address}, {city}, {state}, {zipcode}'.format(address=self.address, city=self.city, state=self.state,
                                                               zipcode=self.zipcode)

    class Meta:
        ordering = ('state', 'city', 'name')


class Jurisdiction(FireCaresBase):
    """
    Models the organizational units such as cities, counties, etc that have many fire stations.
    """

    STATES_CHOICES = [(state.abbr, state.name) for state in us.states.STATES]

    FCODE_CHOICES = [(61200, 'County'),
                     (61201, 'Borough'),
                     (61210, 'City and Borough'),
                     (61202, 'District'),
                     (61203, 'Independent City'),
                     (61204, 'Island'),
                     (61205, 'Judicial Division'),
                     (61206, 'Municipality'),
                     (61207, 'Municipio'),
                     (61208, 'Parish'),
                     (61299, 'Other County Equivalent Area')]

    DATA_SECURITY_CHOICES = [(0, 'Unknown'),
                             (1, 'Top Secret'),
                             (2, 'Secret'),
                             (3, 'Confidential'),
                             (4, 'Restricted'),
                             (5, 'Unclassified'),
                             (6, 'Sensitive')]

    DISTRIBUTION_POLICY_CHOICES = [('A1', 'Emergency Service Provider - Internal Use Only'),
                                   ('A2', 'Emergency Service Provider - Bitmap Display Via Web'),
                                   ('A3', 'Emergency Service Provider - Free Distribution to Third Parties'),
                                   ('A4', 'Emergency Service Provider - Free Distribution to Third Parties Via '
                                          'Internet'),
                                   ('B1', 'Government Agencies or Their Delegated Agents - Internal Use Only'),
                                   ('B2', 'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'),
                                   ('B3', 'Government Agencies or Their Delegated Agents - Free Distribution to Third '
                                          'Parties'),
                                   ('B4', 'Government Agencies or Their Delegated Agents - Free Distribution to Third '
                                          'Parties Via Internet'),
                                   ('C1', 'Other Public or Educational Institutions - Internal Use Only'),
                                   ('C2', 'Other Public or Educational Institutions - Bitmap Display Via Web'),
                                   ('C3', 'Other Public or Educational Institutions - Free Distribution to Third '
                                          'Parties'),
                                   ('C4', 'Other Public or Educational Institutions - Free Distribution to Third '
                                          'Parties Via Internet'),
                                   ('D1', 'Data Contributors - Internal Use Only'), ('D2', 'Data Contributors - '
                                                                                           'Bitmap Display Via Web'),
                                   ('D3', 'Data Contributors - Free Distribution to Third Parties'),
                                   ('D4', 'Data Contributors - Free Distribution to Third Parties Via Internet'),
                                   ('E1', 'Public Domain - Internal Use Only'), ('E2', 'Public Domain - Bitmap '
                                                                                       'Display Via Web'),
                                   ('E3', 'Public Domain - Free Distribution to Third Parties'),
                                   ('E4', 'Public Domain - Free Distribution to Third Parties Via Internet')]

    objectid = models.IntegerField(unique=True, null=True, blank=True)
    permanent_identifier = models.CharField(max_length=40, null=True, blank=True)
    source_featureid = models.CharField(max_length=40, null=True, blank=True)
    source_datasetid = models.CharField(max_length=40, null=True, blank=True)
    source_datadesc = models.CharField(max_length=100, null=True, blank=True)
    source_originator = models.CharField(max_length=130, null=True, blank=True)
    data_security = models.IntegerField(blank=True, null=True, choices=DATA_SECURITY_CHOICES)
    distribution_policy = models.CharField(max_length=4, choices=DISTRIBUTION_POLICY_CHOICES, null=True, blank=True)
    loaddate = models.DateTimeField(null=True, blank=True)
    ftype = models.CharField(blank=True, null=True, max_length=50)
    fcode = models.IntegerField(blank=True, null=True, choices=FCODE_CHOICES)
    state_fipscode = models.CharField(max_length=2, null=True, blank=True)
    state_name = models.CharField(max_length=120, null=True, blank=True)
    county_fipscode = models.CharField(max_length=3, null=True, blank=True)
    county_name = models.CharField(max_length=120, null=True, blank=True)
    population = models.IntegerField(blank=True, null=True)
    gnis_id = models.CharField(max_length=10, null=True, blank=True)
    fips = models.CharField(max_length=10, blank=True, null=True)
    globalid = models.CharField(max_length=38, null=True, blank=True)
    geom = models.PolygonField()

    objects = models.GeoManager()

    @property
    def origin_uri(self):
        """
        This object's URI (from the national map).
        """
        return 'http://services.nationalmap.gov/arcgis/rest/services/govunits/MapServer/13/{0}?f=json' \
            .format(self.objectid)

    @classmethod
    def load_data(cls):
        from django.contrib.gis.geos import LinearRing, Polygon
        objects = requests.get('http://services.nationalmap.gov/arcgis/rest/services/govunits/MapServer/13/query?'
                               'where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&'
                               'spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&'
                               'maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=true&returnCountOnly=false&'
                               'orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&'
                               'gdbVersion=&returnDistinctValues=false&f=json')

        current_ids = set(cls.objects.all().values_list('objectid', flat=True))
        object_ids = set(json.loads(objects.content)['objectIds']) - current_ids
        url = 'http://services.nationalmap.gov/arcgis/rest/services/govunits/MapServer/13/{0}?f=json'

        for object in object_ids:
            try:

                if cls.objects.filter(objectid=object):
                    continue

                obj = requests.get(url.format(object))
                obj = json.loads(obj.content)
                data = dict((k.lower(), v) for k, v in obj['feature']['attributes'].iteritems())

                for key in data.keys():
                    if key not in [field.name for field in cls._meta.fields]:
                        data.pop(key)

                if obj['feature'].get('geometry'):
                    poly = map(LinearRing, obj['feature']['geometry']['rings'])
                    data['geom'] = Polygon(*poly)

                data['loaddate'] = datetime.datetime.fromtimestamp(data['loaddate']/1000.0)
                feat = cls.objects.create(**data)
                feat.save()
                print 'Saved object: {0}'.format(data.get('name'))
                print '{0} Counties loaded.'.format(cls.objects.all().count())

            except KeyError:
                print '{0} failed.'.format(object)
                print url.format(object)

            except IntegrityError:
                print '{0} failed.'.format(object)
                print url.format(object)
                print sys.exc_info()

                try:
                    rollback()
                except:
                    pass

            except:
                print '{0} failed.'.format(object)
                print url.format(object)
                print sys.exc_info()

    class Meta:
        ordering = ('state_name', 'county_name')

    def __unicode__(self):
        return u'{name}, {state}'.format(name=self.county_name, state=self.state_name)


class FireStation(USGSStructureData, FireCaresBase):
    """
    Fire Stations.
    """

    jurisdiction = models.ForeignKey(Jurisdiction, null=True, blank=True)
    fips = models.CharField(max_length=10, blank=True, null=True)
    station_number = models.IntegerField(null=True, blank=True)
    district = models.PolygonField(null=True, blank=True)
    objects = models.GeoManager()

    @property
    def origin_uri(self):
        """
        This object's URI (from the national map).
        """
        return 'http://services.nationalmap.gov/arcgis/rest/services/structures/MapServer/7/{0}?f=json' \
            .format(self.objectid)

    @classmethod
    def load_data(cls):
        objects = requests.get('http://services.nationalmap.gov/arcgis/rest/services/structures/MapServer/7/query?'
                               'where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&'
                               'spatialRel=esriSpatialRelIntersects&relationParam=&outFields=&returnGeometry=true&'
                               'maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=true&returnCountOnly=false&'
                               'orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&'
                               'gdbVersion=&returnDistinctValues=false&f=json')

        current_ids = set(FireStation.objects.all().values_list('objectid', flat=True))
        object_ids = set(json.loads(objects.content)['objectIds']) - current_ids
        url = 'http://services.nationalmap.gov/arcgis/rest/services/structures/MapServer/7/{0}?f=json'

        for object in object_ids:
            try:

                if FireStation.objects.filter(objectid=object):
                    continue

                obj = requests.get(url.format(object))
                obj = json.loads(obj.content)
                data = dict((k.lower(), v) for k, v in obj['feature']['attributes'].iteritems())

                if obj['feature'].get('geometry'):
                    data['geom'] = Point(obj['feature']['geometry']['x'], obj['feature']['geometry']['y'])

                data['loaddate'] = datetime.datetime.fromtimestamp(data['loaddate']/1000.0)
                feat = cls.objects.create(**data)
                feat.save()
                print 'Saved object: {0}'.format(data.get('name'))
                print '{0} Firestations loaded.'.format(FireStation.objects.all().count())

            except KeyError:
                print '{0} failed.'.format(object)
                print url.format(object)

            except IntegrityError:
                print '{0} failed.'.format(object)
                print url.format(object)
                print sys.exc_info()

                try:
                    rollback()
                except:
                    pass

            except:
                print '{0} failed.'.format(object)
                print url.format(object)
                print sys.exc_info()

    class Meta:
        verbose_name = 'Fire Station'


class ResponseCapability(FireCaresBase):
    """
    Models response capabilities (apparatus and responders).
    """
    APPARATUS_CHOICES = [('Engine', 'Engine'),
                         ('Ladder/Truck/Aerial', 'Ladder/Truck/Aerial'),
                         ('Quint', 'Quint'),
                         ('Ambulance/ALS', 'Ambulance/ALS'),
                         ('Ambulance/BLS', 'Ambulance/BLS'),
                         ('Heavy Rescue', 'Heavy Rescue'),
                         ('Boat', 'Boat'),
                         ('Hazmat', 'Hazmat'),
                         ('Chief', 'Chief'),
                         ('Other', 'Other')]

    int_field_defaults = dict(null=True, blank=True, max_length=2, default=0)

    firestation = models.ForeignKey(FireStation)
    apparatus = models.CharField(choices=APPARATUS_CHOICES, max_length=20, default='Engine')
    firefighter = models.IntegerField(**int_field_defaults)
    firefighter_emt = models.IntegerField(verbose_name='Firefighter EMT', **int_field_defaults)
    firefighter_paramedic = models.IntegerField(verbose_name='Firefighter Paramedic', **int_field_defaults)
    ems_emt = models.IntegerField(verbose_name='EMS-Only EMT', **int_field_defaults)
    ems_paramedic = models.IntegerField(verbose_name='EMS-Only Paramedic', **int_field_defaults)
    officer = models.IntegerField(verbose_name='Company/Unit Officer', **int_field_defaults)
    officer_paramedic = models.IntegerField(verbose_name='Company/Unit Officer Paramedic', **int_field_defaults)
    ems_supervisor = models.IntegerField(verbose_name='EMS Supervisor', **int_field_defaults)
    chief_officer = models.IntegerField(verbose_name='Cheif Officer', **int_field_defaults)

    def __unicode__(self):
        return '{0} response capability for {1}'.format(self.apparatus, self.firestation)

    class Meta:
        verbose_name_plural = 'Response Capabilities'


