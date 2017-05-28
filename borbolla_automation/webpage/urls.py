import sistema.views 
from sistema.printing import printing


from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url(r'^$', sistema.views.print_users, name='print'),
    url(r'^admin/', admin.site.urls),
]