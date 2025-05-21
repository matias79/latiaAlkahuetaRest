from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Aplicaciones.restaurant.models import Menu

# Create your views here.
def inicio(request):
    return render(request, 'restaurant/inicio.html')

#listar menus

def todo_menu(request):
    menus = Menu.objects.all()
    context = {'menu':menus}
    return render(request, 'restaurant/menus.html', context)

@login_required(login_url='/login/')
def tabla_menu(request):
    tablamen=Menu.objects.all()
    context={'menu':tablamen}
    return render(request, 'restaurant/tablamenus.html', context)

@login_required(login_url='/login/')
def eliminar_menu(request, id):
    menu = Menu.objects.get(idMenu=id)
    menu.delete()
    messages.success(request, 'Menu Eliminada Correctamente')
    return redirect('/menu')

@login_required(login_url='/login/')
def crear_menu(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        detalle = request.POST['detalle']
        precio = request.POST['precio']
        imagen = request.POST['imagen']
        Menu.objects.create(nombreMenu = nombre, detalleMenu = detalle, precioMenu = precio,  imagenMenu = imagen)
        messages.success(request, 'Menu Creado Correctamente')
        return redirect('/menu')
    else:
        return render(request, 'restaurant/crear_menu.html')

@login_required(login_url='/login/')
def modificar_menu(request, id):
    if request.method == 'POST':
        if request.POST.get("nombre") and request.POST.get("detalle") and request.POST.get("precio") and request.POST.get("imagen"):
            menu = Menu.objects.get(idMenu=id)
            menu.nombreMenu=request.POST.get("nombre")
            menu.detalleMenu=request.POST.get("detalle")
            menu.precioMenu=request.POST.get("precio")
            menu.imagenMenu=request.POST.get("imagen")
            menu.save()
            messages.success(request, 'Menu Modificado Correctamente')
            return redirect('/tabla_menu')
        
    else:
        menus =Menu.objects.filter(idMenu=id)
        return render(request, 'restaurant/modificar_menu.html',{'menus':menus})
    

    