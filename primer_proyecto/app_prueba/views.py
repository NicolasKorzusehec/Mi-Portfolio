import os

from django.shortcuts import render, redirect
from django.urls import reverse
#para crear usuarios
from django.contrib.auth.models import User

# el form del registro
from .forms import RegistroForm


# Create your views here.

#Vamos a agregar un conteo de visitas al home, agregamos en la función que renderiza la home el contador. Para eso obtenemos el valor de la clave de sesión num_visits, estableciendo el valor a 0 si no había sido establecido previamente. Cada vez que se recibe la solicitud, incrementamos el valor y lo guardamos de vuelta en la sesión (para la siguiente vez que el usuario visita la página).
def home(request):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits':num_visits}

    if request.user.username:
        return render(request, os.path.join("app_prueba","home.html"), {'name' : request.user.username})
    else:    
        return render(request, os.path.join("app_prueba","home.html"), context=context)

def about(request):
    return render(request, os.path.join("app_prueba","about.html"))

def portfolio(request):
    return render(request, os.path.join("app_prueba","portfolio.html"))

def contact(request):
    return render(request, os.path.join("app_prueba","contact.html"))

def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        #Traemos los datos enviados
        registro_form = registro_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if registro_form.is_valid():
            cliente_id= request.POST.get('cliente_id','')
            email = request.POST.get('email','')
            pwd = request.POST.get('pwd','')
            print(cliente_id,email,pwd)

            user = User.objects.create_user(cliente_id, email, pwd)
            user.save()
            print('creado')
        #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('login'))
    
    return render(request, os.path.join("app_prueba","registro.html"),{'form': registro_form})
