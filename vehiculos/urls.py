from django.urls import path
from vehiculos import views

urlpatterns = [
    path('saludos/', views.saludar),
    path('estatico/', views.crear_estatico),
    path('mostrar/', views.mostrar),
    path('dinamico/', views.crear_dinamico),
]
