from django import forms
from datetime import date
""" Es parecido a crear un modelo, ya que debemos indicar los campos y su tipo. El nuestro tiene tres:

Nombre: que será una cadena de texto.
Email: que tiene su propio tipo.
Contenido: """

class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())
    """ Los campos vienen definidos en el módulo forms y para el nombre se utiliza el atributo label. Por defecto estos campos se renderizan como tags , pero se pueden cambiar estableciendo un tipo de widget, como en el caso el contenido donde queremos mostrar un tag <textarea>. """
    
    #probamos que pasa si agregamos los campos de fechas y un selector.
    day = forms.DateField(initial=date.today())

    lista=[('A','30 Cuotas'),  ('B','60 Cuotas'), ('C', '90 Cuotas')]
    item_lista= forms.CharField(label='Que opciones elegis?', widget=forms.Select(choices=lista))