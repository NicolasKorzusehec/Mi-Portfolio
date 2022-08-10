"""primer_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

##primer_proyecto/urls.py

#del modulo app_prueba (fijarse que tiene __init.py__) importamos el módulo views 
#es decir, de la app prueba importamos las vistas. 
from app_prueba import views as pruebas_views

urlpatterns = [
    #Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos 
    # a la vista views.home que tiene el nombre home.
    path('',pruebas_views.home, name="home"), 
    path('',pruebas_views.about, name="about"), 
    path('',pruebas_views.portfolio, name="portfolio"), 
    path('',pruebas_views.contact, name="contact"), 

    path('admin/', admin.site.urls),
]
