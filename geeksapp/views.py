from django.shortcuts import render
from .models import *
# Create your views here.
def inicio(request):
    
    servicios = Servicios.objects.all()
    
    
    
    hoy = 3
    context = {
        'hoy':hoy,
        'servicios':servicios,
    }
    return render(request, 'inicio.html', context=context)



def servicio(request, slug):
    servicios = Servicios.objects.all().exclude(slug=slug)
    servicio=Servicios.objects.get(slug=slug)
    
    try:
        next_ = Servicios.objects.get(id = servicio.pk + 1)
        print(next_)
        
    except Servicios.DoesNotExist:
        next_ = Servicios.objects.get(id = 2)

    
    context = {
        'servicios':servicios,
        'servicio':servicio,
        'next': next_
    }
    return  render(request, 'servicio.html', context=context)