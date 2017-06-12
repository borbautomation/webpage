from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length = 128 , unique = True)
    estado = models.CharField(max_length = 15, default = 'None')
    ciudad = models.CharField(max_length = 15,default = 'None')
    fecha_creacion = models.DateField( auto_now_add = True)
    ultima_modificacion = models.DateField( auto_now = True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length = 128 , )
    telefono = models.CharField(max_length = 20 ,)
    extension = models.IntegerField(default = 0 ,)
    email = models.CharField(max_length = 50 ,)
    departamento = models.CharField(max_length = 28)
    cliente = models.ForeignKey(Cliente)
    fecha_creacion = models.DateField(auto_now_add = True)
    ultima_modificacion = models.DateField(auto_now = True)

    def __str__(self):
        return '%s %s'%(self.nombre , self.telefono)    


class Cotizacion(models.Model):
    fecha = models.DateField( auto_now_add = True)
    contacto = models.ForeignKey(Contacto)
    aceptada = models.BooleanField()
    importe = models.IntegerField()
    cantidad_pagada = models.IntegerField(default = 0)
    ultima_modificacion = models.DateField( auto_now = True)

    class Meta:
        verbose_name_plural = 'Cotizaciones'
    
    def __str__(self):
        return '%s %s %s'%(self.contacto.cliente.nombre , self.contacto.nombre ,self.importe )

class Producto(models.Model):
    descripcion = models.CharField(max_length = 128)
    precio = models.IntegerField()
    fecha = models.DateField(auto_now_add = True)
    ultima_modificacion = models.DateField(auto_now = True)
    def __str__(self):
        return '%s %s'%(self.descripcion , self.precio) 

class Partida(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)              
    cotizacion = models.ForeignKey(Cotizacion)
    fecha = models.DateField( auto_now_add = True)
    ultima_modificacion = models.DateField(auto_now = True)

    def __str__(self):
        return '%s %s %s'%(self.cantidad , self.producto.descripcion , self.producto.precio)





# Create your models here.
