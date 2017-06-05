from django.contrib import admin

from dollar.models import *

class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,)
    search_fields = ('nombre' , 'fecha_creacion')

class PrecioAdmin(admin.ModelAdmin):
    list_display = ('get_nombre' , 'compra','venta','fecha_creacion','ultima_modificacion')
    search_fields = ('banco__nombre' , 'fecha_creacion')
    def get_nombre(self,obj):
        return obj.banco.nombre

    get_nombre.admin_order_field  = 'nombre'  #Allows column order sorting
    get_nombre.short_description = 'Cliente de Contacto'  #Renames column head  

admin.site.register(Banco,BancoAdmin)
admin.site.register(Precio,PrecioAdmin)    

