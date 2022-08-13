from django.shortcuts import render
from .models import Proyectos
import os

# Create your views here.

#Recuperamos los registros de la tabla Proyectos que maneja nuestro modelo ORM a través de una lista de objetos interna y un método .all() que hace referencia a todos sus objetos.
#Debemos inyectar estos proyectos en el template, para hacerlo simplemente enviamos a la función render un tercer parámetro con un diccionario y los valores que queremos inyectar.

def portfolio(request):
    projects = Proyectos.objects.all() 
    return render(request, os.path.join("portfolio","portfolio.html"), {'projects': projects})

