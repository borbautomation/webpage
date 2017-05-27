from django.contrib import admin

from sistema.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'estado' , 'ciudad',)
    search_fields = ('nombre' , 'estado' , 'ciudad',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,'cliente', 'departamento' , 'telefono' , 'extension' )
    search_fields = ('nombre' , 'cliente__nombre')
    #filter_horizontal = ('cliente')
    raw_id_fields = ('cliente',)    

class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('get_cliente' ,'get_contacto', 'fecha' , 'importe' , 'id' )
    search_fields = ('fecha' , 'contacto__cliente__nombre','contacto__nombre')
    #filter_horizontal = ('partida',)
    #filter_horizontal = ('cliente')
    raw_id_fields = ('contacto',)    

    def get_cliente(self,obj):
        return obj.contacto.cliente.nombre

    def get_contacto(self,obj):
        return obj.contacto.nombre

    get_cliente.admin_order_field  = 'nombre'  #Allows column order sorting
    get_cliente.short_description = 'Cliente de Contacto'  #Renames column head         
    
    get_contacto.admin_order_field  = 'nombre'  #Allows column order sorting
    get_contacto.short_description = 'Nombre de Contacto' #Renames column head 

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('id','cantidad','get_descripcion','get_precio')
    #filter_horizontal = ('producto',)
    search_fields = ('producto__descripcion',)

    def get_descripcion(self,obj):
        return obj.producto.descripcion

    def get_precio(self,obj):
        return obj.producto.precio
    
    get_descripcion.admin_order_field  = 'descripcion'  #Allows column order sorting
    get_descripcion.short_description = 'Descripcion desde producto'  #Renames column head         
    
    get_precio.admin_order_field  = 'precio'  #Allows column order sorting
    get_precio.short_description = 'precio de producto' #Renames column head 



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','precio')
    search_fields = ('descripcion',)

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Cotizacion,CotizacionAdmin)
admin.site.register(Partida,PartidaAdmin)
admin.site.register(Producto,ProductoAdmin)

# Register your models here.
