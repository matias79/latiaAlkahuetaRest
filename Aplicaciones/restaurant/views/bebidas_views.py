from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from Aplicaciones.restaurant.models import Bebida
from django.contrib.auth.decorators import login_required
# Create your views here.


#listar bebidas

def todo_bebidas(request):
    bebida = Bebida.objects.all()
    context = {'bebida':bebida}
    return render(request, 'restaurant/bebidas/bebidas.html', context)

@login_required(login_url='/login/')
def tabla_bebidas(request):
    tablabebida =Bebida.objects.all()
    context={'bebida':tablabebida}
    return render(request, 'restaurant/bebidas/tablabebidas.html', context)

@login_required(login_url='/login/')
def eliminar_bebida(request, id):
    bebida = Bebida.objects.get(idbebida=id)
    bebida.delete()
    messages.success(request, 'Bebida Eliminada Correctamente')
    return redirect('/bebidas')

@login_required(login_url='/login/')
def crear_bebida(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        detalle = request.POST['detalle']
        precio = request.POST['precio']
        imagen = request.POST['imagen']
        Bebida.objects.create(nombre = nombre, descripcion = detalle, precio = precio,  imagen = imagen)
        messages.success(request, 'Bebida Creada Correctamente')
        return redirect('/bebidas')
    else:
        return render(request, 'restaurant/bebidas/crear_bebidas.html')

@login_required(login_url='/login/')
def modificar_bebida(request, id):
    if request.method == 'POST':
        if request.POST.get("nombre") and request.POST.get("detalle") and request.POST.get("precio") and request.POST.get("imagen"):
            bebida = Bebida.objects.get(idbebida=id)
            bebida.nombre=request.POST.get("nombre")
            bebida.descripcion=request.POST.get("detalle")
            bebida.precio=request.POST.get("precio")
            bebida.imagen=request.POST.get("imagen")
            bebida.save()
            messages.success(request, 'Bebida Modificada Correctamente')
            return redirect('/tabla_bebidas')
        
    else:
        bebi =Bebida.objects.filter(idbebida=id)
        return render(request, 'restaurant/bebidas/modificar_bebida.html',{'bebida':bebi})
    

    