from django.contrib import admin
from django.urls import path, include
from anggota.views import input_view


urlpatterns = [
    path('', input_view, name='input-view-index'),
    path('admin/', admin.site.urls),
    path('api/', include('anggota.urls'))
]
