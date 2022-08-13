from django.shortcuts import render
import os

# Create your views here.

def contact(request):
    return render(request, os.path.join("contact","contact.html"))
