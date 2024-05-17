from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    slug = models.SlugField(max_length=350, unique=True, null=True, editable=False)
    portada = models.ImageField('Portada', null=True, upload_to='portadas/')
    icono = models.ImageField('Icono', upload_to='iconos/')
    contenido = RichTextField('Contenido')
    
    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
  
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('servicio', kwargs=kwargs)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Informacion(models.Model):
    telefono = models.CharField('Número de teléfono', max_length=40)
    email = models.EmailField('Correo Electrónico')
    web = models.CharField('Página web', max_length=50)

    def __str__(self):
        return 'Información de Geeks'
    
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Información'