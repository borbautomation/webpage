from django.db import models

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length = 128 , )
    compania = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 50 )
    text = models.TextField()
    fecha = models.DateField(auto_now_add = True)

    def __str__(self):
        return '%s %s %s'%(self.nombre , self.compania , self.email)  


# Create your models here.
