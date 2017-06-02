from django.db import models

# Create your models here.


class Banco(models.Model):
    nombre = models.CharField(max_length = 128 , unique = True)
    fecha_creacion = models.DateField( auto_now_add = True)
    ultima_modificacion = models.DateField( auto_now = True)

    def __str__(self):
        return self.nombre

class Precio(models.Model):
    banco = models.ForeignKey(Banco)
    compra = models.FloatField()
    venta = models.FloatField()
    fecha_creacion = models.DateField( auto_now_add = True)
    ultima_modificacion = models.DateField( auto_now = True)
    

    def __str__(self):
        return ('%s %s %s')%(self.banco.nombre, self.compra, self.venta) 