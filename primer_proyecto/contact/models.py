from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre") #agregamos el campo verbose para describir
    email = models.EmailField(max_length=200, verbose_name="Email")
    content =  models.TextField(max_length=200, verbose_name="Contenido")

    class Meta():
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        #ordering = ["-created"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.name

