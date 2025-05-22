from django.http import HttpResponse
from django.shortcuts import redirect, render
from Aplicaciones.restaurant.models import AlmuerzoEjecu
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def almuerEjec(request):
    almuerzo = AlmuerzoEjecu.objects.all()
    return render(request,'restaurant/almuerzos/ejecutivo.html', {'almuerzo':almuerzo})

@login_required(login_url='/login')
def tabla_almuerzo(request):
    almuerzo = AlmuerzoEjecu.objects.all()
    context={'almuerzo':almuerzo}
    return render(request, 'restaurant/almuerzos/tablaalmuerzos.html', context)

@login_required(login_url='/login')
def eliminar_almuerzo(request, id):
    almuerzo = AlmuerzoEjecu.objects.get(pk=id)
    almuerzo.delete()
    messages.success(request, 'Almuerzo Eliminado correctamente')
    return redirect('/almuerzos')

@login_required(login_url='/login')
def crear_almuerzo(request):
    if request.method == 'POST':
        sopa=request.POST.get('sopa')
        principio=request.POST.get('principio')
        carne=request.POST.get("carne")
        bebida=request.POST.get("bebida")
        imagensopa=request.POST.get('imagensopa')
        imagenbandeja=request.POST.get('imagenbandeja')
        AlmuerzoEjecu.objects.create(sopas=sopa, principio=principio, carnes=carne, bebida=bebida, imagenSopa=imagensopa, imagenBandeja=imagenbandeja)
        messages.success(request, 'Almuerzo creado correctamente')
        return redirect('/almuerzos')
    else:
        return render(request, 'restaurant/almuerzos/crear_almuerzo.html')

@login_required(login_url='/login')
def editar_almuerzo(request, id):
    if request.method == 'POST':
        if request.POST.get("sopa") and request.POST.get ("principio") and request.POST.get ("carne") and request.POST.get ("bebida") and request.POST.get ("imagensopa") and request.POST.get ("imagenbandeja"):
            almu=AlmuerzoEjecu.objects.get(id=id)
            almu.sopas=request.POST.get("sopa")
            almu.principio=request.POST.get ("principio")
            almu.carnes=request.POST.get ("carne")
            almu.bebida=request.POST.get ("bebida")
            almu.imagenSopa=request.POST.get ("imagensopa")
            almu.imagenBandeja=request.POST.get ("imagenbandeja")
            almu.save()
            messages.success(request, 'Almuerzo editado correctamente')
            return redirect('/almuerzos')
    else:
        almuerzo = AlmuerzoEjecu.objects.filter(id=id)
        return render(request, 'restaurant/almuerzos/modificar_almuerzo.html', {'almuerzo': almuerzo})
    

      