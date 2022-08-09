from django.db import models

# Create your models here.

"""
```bash
python3 manage.py makemigrations portfolio
python3 manage.py migrate portfolio 
```
Cada vez que hagamos un cambio en nuestro archivo models.py tenemos que ejecutar estos dos comandos para crear una migración y posteriormente aplicarla.
"""

#agregamos los atributos con el tipo de datos de Models
#cada atributo es un campo
class Proyectos(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") #agregamos el campo verbose para describir
    description =  models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
    #el atributo upload_to, permite indicar donde subir las imagenes
    link = models.URLField(null=True, blank=True, verbose_name="Enlace Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta():
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente

    def __str__(self): 
        return self.title

