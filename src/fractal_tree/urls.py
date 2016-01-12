from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='fractal-tree-index'),

]