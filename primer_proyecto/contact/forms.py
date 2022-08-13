from django import forms

""" Es parecido a crear un modelo, ya que debemos indicar los campos y su tipo. El nuestro tiene tres:

Nombre: que será una cadena de texto.
Email: que tiene su propio tipo.
Contenido: """

class ContactoFrom(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())