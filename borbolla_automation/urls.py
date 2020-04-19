from webpage.views import *
from api import views

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^webpage/', include('webpage.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^api/', include('api.urls')),
]