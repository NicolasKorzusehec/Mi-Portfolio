import imp
import os

from django.shortcuts import render
from .models import Proyectos
#importamos el decorador para autenticacion de usuarios
from django.contrib.auth.decorators import login_required


# Create your views here.

#Recuperamos los registros de la tabla Proyectos que maneja nuestro modelo ORM a través de una lista de objetos interna y un método .all() que hace referencia a todos sus objetos.
#Debemos inyectar estos proyectos en el template, para hacerlo simplemente enviamos a la función render un tercer parámetro con un diccionario y los valores que queremos inyectar.

#usamos el decorador
@login_required
def portfolio(request):
    projects = Proyectos.objects.all() 
    return render(request, os.path.join("portfolio","portfolio.html"), {'projects': projects})

#La forma más fácil para restringir el acceso a tus funciones es aplicar login_required a tu función de vista. Si el usuario ha iniciado sesión entonces tu código de vista se ejecutará como normalmente lo hace. Si el usuario no ha iniciado sesión, se redirigirá a la URL de inicio de sesión definida en tu configuración de proyecto (settings.LOGIN_URL), pasando el directorio absoluto actual como el parámetro URL next.