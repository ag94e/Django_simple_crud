from django.urls import path
from . import views

app_name = 'inventarios'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar, name='agregar'),
    path('modificar/<int:pk>/', views.modificar, name='modificar'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),
]
