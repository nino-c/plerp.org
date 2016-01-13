from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import profiles.urls
import accounts.urls
import deployments.urls
import fractal_tree.urls
#import canvasapp.urls
import portfolio.urls

from . import views

urlpatterns = [
    url(r'^$', portfolio.views.mainindex, name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^portfolio/', include(portfolio.urls, namespace='portfolio')),
    url(r'^fractal_tree/', include(fractal_tree.urls, namespace='fractal_tree')),
    #url(r'^canvasapp/', include(canvasapp.urls, namespace='canvasapp')),
    url(r'^deployments/', include(deployments.urls, namespace='deployments')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


