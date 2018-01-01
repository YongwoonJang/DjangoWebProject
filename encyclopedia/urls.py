from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload_file, name='upload_file'),
    url(r'^static/encyclopedia/sourcestorage/codeinventory/[0-9]+$', views.page, name='page'),
]
