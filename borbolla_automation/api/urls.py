from api import views

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    
]