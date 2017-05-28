from sistema import views
from sistema.printing import printing
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^print/', sistema.views.print_users),
       
]