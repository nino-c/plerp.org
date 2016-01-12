from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<name>[a-zA-Z0-9\-]*)/$', views.list_category, name='list-category'),

]