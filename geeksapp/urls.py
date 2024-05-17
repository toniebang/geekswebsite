from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicio/<slug:slug>', views.servicio, name='servicio')
]