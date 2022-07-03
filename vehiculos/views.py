from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import carros

# Create your views here.

def saludar(request):
    
    return HttpResponse("Bienvenido a mi primer URL")


def crear_estatico(request):
    
    objeto = carros( marca = "Mazda" , color = "Blanco" , cantidad_pasajeros = 5 , fecha_salida = "2021-11-13" )
    objeto.save()
    
    return HttpResponse("Datos cargados con exito")


def crear_dinamico(request):
    
    if request.GET:
        
        marcas = str( request.GET['marcas'] )
        
        colores = str( request.GET['colores'] )
        
        cantidad = int( request.GET['cantidad'] )
        
        fecha = str( request.GET['fecha'] )
        
        objeto2 = carros( marca = marcas , color = colores , cantidad_pasajeros = cantidad , fecha_salida = fecha )
        objeto2.save()
    
    
    info = carros.objects.all()
    contexto = { "vehiculos" : info }
    
    plantilla = loader.get_template("crear.html")
    documento = plantilla.render( contexto )
    
    
    return HttpResponse( documento )
        

def mostrar(request):
    
    info = carros.objects.all()
    contexto = { "vehiculos" : info }
    
    plantilla = loader.get_template("mostrar.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )
