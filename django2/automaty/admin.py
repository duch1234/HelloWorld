from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django.http import HttpResponse
# Register your models here.

from automaty.models import dekoders
from automaty.models import karta
from automaty.models import endurance
from automaty.models import export_csv
from automaty.models import export_xlsx
from automaty.models import setAsDone
class CityAdmin(ModelAdmin):

    list_display = ('dekoderName', 'serialNumber','dekoderVersion','pub_date')
#     list_filter = (
#         ('dekoderName',admin.RelatedOnlyFieldListFilter),
#         )
    list_filter=('dekoderName','dekoderVersion')
    search_fields = ('dekoderName', 'serialNumber', 'dekoderVersion' )
admin.site.register(dekoders,CityAdmin)


class KartaAdmin(ModelAdmin):

    list_display = ('kartaName', 'serialNumber','kartaVersion','kartaOwner','kartaCurrentOwner')
    actions = [export_csv,export_xlsx]



   
admin.site.register(karta, KartaAdmin)


class enduranceAdmin(ModelAdmin):
    list_display = ('dekoderName', 'serialNumber','RaVersion','FWversion','comment','StartDate','EndDate','statusField')
    search_fields = ('dekoderName', 'serialNumber','RaVersion','FWversion','comment','StartDate','EndDate','statusField' )
    
    list_filter=('dekoderName','RaVersion','RaVersion','FWversion','StartDate')
    actions = [setAsDone]

admin.site.register(endurance, enduranceAdmin)