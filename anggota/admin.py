from django.contrib import admin
from .models import Anggota, Pengusul, Wilayah
from import_export.admin import ExportActionMixin


class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['nia', 'nama', 'wilayah']
    search_fields = ['nama']


class PengusulAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['anggota', 'email', 'mobile', 
                    'penatua_1', 'penatua_alasan_1','penatua_mobile_1',
                    'penatua_2', 'penatua_alasan_2','penatua_mobile_2',
                    'penatua_3', 'penatua_alasan_3','penatua_mobile_3',
                    'penatua_4', 'penatua_alasan_4','penatua_mobile_4',
                    'penatua_5', 'penatua_alasan_5','penatua_mobile_5' ]

class WilayahAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama']

admin.site.site_header = 'Admin Pencalonan Penatua'
admin.site.site_title =  'Pencalonan Penatua GKI Serpong'
admin.site.index_title =  'Pencalonan Penatua GKI Serpong'

admin.site.register(Anggota, AnggotaAdmin)
admin.site.register(Pengusul, PengusulAdmin)
admin.site.register(Wilayah, WilayahAdmin)
