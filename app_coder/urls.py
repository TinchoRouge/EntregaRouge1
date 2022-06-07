from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("contacto" , views.contacto),
    #path("alta_curso/<nombre>" , views.alta_curso),
    path("alta_curso" , views.curso_formulario , name="alta_curso"),
    path("buscar_curso" , views.buscar_curso , name="buscar_curso"),
    path("buscar" , views.buscar),
    path("alta_profesores" , views.alta_profesores , name="alta_profesores"),
    path("alta_alumnos" , views.alta_alumnos , name="alta_alumnos"),
    path("buscar_profesores" , views.buscar_profesores , name="buscar_profesores"),
    path("busqueda_profesores" , views.busqueda_profesores ),
    path("buscar_alumnos" , views.buscar_alumnos , name="buscar_alumnos"),
    path("busqueda_alumnos" , views.busqueda_alumnos)
    ]
