from django.contrib import admin

# Register your models here.





#Todavía no se ve la tabla proyecto que creamos, porque no la registramos en el admin de nuestra app portfolio.

##portfolio/admin.py
from .models import Proyectos
# Register your models here.
admin.site.register(Proyectos)

#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Project)
