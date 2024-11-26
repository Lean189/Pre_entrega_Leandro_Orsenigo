from django.urls import path
from datos import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('agregar_curso/', views.agregar_curso, name= 'agregar_curso'),
    path("agregar_estudiante/",views.agregar_estudiante , name="agregar_estudiante"),
    path('agregar_profesor/', views.agregar_profesor, name= 'agregar_profesor'),
    path('busqueda_camada', views.busqueda_camada, name= 'busqueda_camada'),
    path('buscar/', views.buscar, name= 'buscar'),
]
