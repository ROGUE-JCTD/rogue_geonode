from .models import FireStation, Jurisdiction, ResponseCapability
from django.contrib.gis import admin


class FireStationAdmin(admin.OSMGeoAdmin):
    list_display = ['state', 'name', 'jurisdiction']
    list_filter = ['state', 'ftype']
    search_fields = ['name', 'state', 'city']
    readonly_fields = ['permanent_identifier', 'source_featureid', 'source_datasetid', 'objectid', 'globalid',
                       'gnis_id', 'foot_id', 'complex_id']


class FireStationInline(admin.TabularInline):
    model = FireStation
    fk_name = 'jurisdiction'
    extra = 0
    readonly_fields = ['permanent_identifier', 'source_featureid', 'source_datasetid', 'objectid', 'globalid',
                       'gnis_id', 'foot_id', 'complex_id']


class JurisdictionAdmin(admin.OSMGeoAdmin):
    list_display = ['state_name', 'county_name', 'fcode']
    list_filter = ['state_name']
    search_fields = ['county_name', 'state_name']
    inlines = [FireStationInline]


class ResponseCapabilityAdmin(admin.OSMGeoAdmin):
    pass


admin.site.register(FireStation, FireStationAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
admin.site.register(ResponseCapability, ResponseCapabilityAdmin)
