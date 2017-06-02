from django.contrib import admin

from dollar.models import *

class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,)
    search_fields = ('nombre' , 'fecha_creacion')

class PrecioAdmin(admin.ModelAdmin):
    list_display = ('banco__nombre' , 'compra','venta')
    search_fields = ('banco__nombre' , 'fecha_creacion')

admin.site.register(Banco,BancoAdmin)
admin.site.register(Precio,PrecioAdmin)    

# Register your models here.
