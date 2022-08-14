from multiprocessing import context
from django.shortcuts import render

from django.shortcuts import HttpResponse

import os


# Create your views here.

#Vamos a agregar un conteo de visitas al home, agregamos en la función que renderiza la home el contador. Para eso obtenemos el valor de la clave de sesión num_visits, estableciendo el valor a 0 si no había sido establecido previamente. Cada vez que se recibe la solicitud, incrementamos el valor y lo guardamos de vuelta en la sesión (para la siguiente vez que el usuario visita la página).
def home(request):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits':num_visits}
    return render(request, os.path.join("app_prueba","home.html"), context=context)

def about(request):
    return render(request, os.path.join("app_prueba","about.html"))

def portfolio(request):
    return render(request, os.path.join("app_prueba","portfolio.html"))

def contact(request):
    return render(request, os.path.join("app_prueba","contact.html"))
