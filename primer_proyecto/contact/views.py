from django.shortcuts import render
from django.urls import reverse
import os


# Create your views here.

#importamos el modulo donde esta la clase ContactForm
from .forms import ContactoForm

def contact(request):
    # Se debe crear una instancia de este formulario en la vista 'contact' y enviarla al template
    contact_form = ContactoForm
    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos losdatos enviados
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            return render(request, os.path.join("contact","contact.html"), {"enviado": name})
    return render(request, os.path.join("contact","contact.html"), {"form": contact_form})
