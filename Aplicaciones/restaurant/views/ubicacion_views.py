#views de datos como contacto, ubicacion quines somos
from django.shortcuts import render


def contacto(request):
    return render(request, 'datos/contact.html')

def latia(request):
    return render(request, 'datos/latia.html')

def ubicacion(request):
    return render(request, 'datos/ubicacion.html')
