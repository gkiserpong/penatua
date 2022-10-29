from django.contrib import admin
from .models import Anggota, Pengusul, Wilayah


class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['nia', 'nama', 'wilayah']
    search_fields = ['nama']


class PengusulAdmin(admin.ModelAdmin):
    list_display = ['anggota', 'email', 'mobile', 'penatua_1', 'penatua_2', 'penatua_3', 'penatua_4', 'penatua_5']

class WilayahAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama']


admin.site.register(Anggota, AnggotaAdmin)
admin.site.register(Pengusul, PengusulAdmin)
admin.site.register(Wilayah, WilayahAdmin)
