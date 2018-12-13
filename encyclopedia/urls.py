from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^favicon.ico$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'encyclopedia/ico/favicon.ico')), #google chrome favicon fix
    url(r'^upload$', views.upload_file, name='upload_file'),
    url(r'^search$', views.search_data, name='search_data'),
    url(r'^static/encyclopedia/sourcestorage/codeinventory/[0-9]+$', views.page, name='page'),
]
