from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Contacto  # Importar el modelo de contact


import os




# Create your views here.

#importamos el modulo donde esta la clase ContactForm
from .forms import ContactoForm

@login_required
def contact(request):
    # Se debe crear una instancia de este formulario en la vista 'contact' y enviarla al template
    contact_form = ContactoForm

    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos losdatos enviados
        comentario = Contacto()
        contact_form = contact_form(data=request.POST)

        if contact_form.is_valid():
            comentario.title = request.POST.get("title", "")
            comentario.name = request.POST.get("name", "")
            comentario.email = request.POST.get("email", "")
            comentario.content = request.POST.get("content", "")
            
            #print(name,email,content)

            #contacto = Contacto.objects.all(name, email, content)

            comentario.save()
            print('creado')
            #En lugar de renderizar el template de prestamo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('contact'))
        
    return render(request, os.path.join("contact","contact.html"), {'form': contact_form})


