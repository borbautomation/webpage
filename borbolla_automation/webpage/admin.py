from django.contrib import admin
from webpage.models import *


class FormularioContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'compania' , 'email','fecha')
    search_fields = ('nombre' , 'compania' , 'email',)



admin.site.register(FormularioContacto,FormularioContactoAdmin)
# Register your models here.
