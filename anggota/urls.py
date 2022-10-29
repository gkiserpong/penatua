from django.urls import path
from .views import get_anggota, input_view, get_pengusul, submit_usulan, get_anggota_detail, get_wilayah


urlpatterns = [
    path('anggota-detail', get_anggota_detail, name='get-anggota-detail'),
    path('anggota', get_anggota, name='get-anggota'),
    path('wilayah', get_wilayah, name='get-wilayah'),
    path('input', input_view, name='input-view'),
    path('pengusul', get_pengusul, name='get-pengusul'),
    path('submit', submit_usulan, name='submit-usulan')
]