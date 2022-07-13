from django.urls import path
from vehiculos import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('saludos/', views.saludar),
    path('estatico/', views.crear_estatico),
    path('mostrar/', views.mostrar, name = "mostrar"),
    path('dinamico/', views.crear_dinamico, name = "crear"),
    path('detail_<int:id>/', views.detail, name="detalles"),
    path('editar_<int:id2>/', views.actualizar, name="actualizar"),
    path('borrar_<int:id2>', views.borrar, name="borrar"),
    path('CRUD/', views.CRUD, name="CRUD"),
    path('buscador/', views.buscar)
]
