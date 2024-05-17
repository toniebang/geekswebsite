from .models import Informacion
def informacion(request):
    
    info = Informacion.objects.all()[:1]
    
    return {
        'info':info,
        
    }