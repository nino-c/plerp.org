from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<name>[a-zA-Z0-9\-]*)/$', views.list_category, name='list-category'),
    url(r'^show/(?P<id>[0-9]*)$', views.show_item, name='show-item'),
]