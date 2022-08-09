from django.shortcuts import render

from django.shortcuts import HttpResponse

import os


# Create your views here.

def home(request):
    """     html_response = "<h1>Bienvenidxs a mi primer sitio hecho con DJANGO!</h1>"
        for i in range(10):
            html_response += "<p>Línea " + str(i) + "</p>"
        return HttpResponse(html_response)
    """
    return render(request, os.path.join("app_prueba","home.html"))

def about(request):
    return render(request, os.path.join("app_prueba","about.html"))

def portfolio(request):
    return render(request, os.path.join("app_prueba","portfolio.html"))

def contact(request):
    return render(request, os.path.join("app_prueba","contact.html"))
