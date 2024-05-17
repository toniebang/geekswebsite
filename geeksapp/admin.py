from django.contrib import admin
from .models import *

# Register your models here.
class Serviciosadmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
class Infoadmin(admin.ModelAdmin):
    list_display = ('telefono', 'email', 'web',)
    
    
admin.site.register(Informacion, Infoadmin)
admin.site.register(Servicios, Serviciosadmin)