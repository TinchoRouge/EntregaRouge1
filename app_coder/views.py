from django.shortcuts import render
from app_coder.models import Curso , Profesor , Alumno
from django.http import HttpResponse
from django.template import loader
from app_coder.forms import Curso_formulario , Profesor_formulario , Alumno_formulario
# Create your views here.


def inicio(request):
    return render(request , "plantillas.html")


#CURSOS

def cursos(request):
    cursos = Curso.objects.all()
    dicc ={"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento= plantilla.render(dicc)
   
    return HttpResponse(documento)


def alta_curso(request):
    if request.method == "POST":
    
        mi_formulario = Curso_formulario(request.POST)


        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
        cursos = Alumno( nombre=datos['nombre'] , camada=datos['camada'])
        cursos.save()
        
        return render(request , "formulario.html")

    return render(request , "formulario.html")

def buscar_curso(request):
    
    return render(request , "buscar_curso.html")

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")      





def contacto(request):
    return render(request , "contacto.html")        

   


def curso_formulario(request):
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)


        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
        curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
        curso.save()
        
        return render(request , "formulario.html")

    return render(request , "formulario.html")    


def alumnos(request):
        return render(request , "alumnos.html")    

#ALUMNOS

def alumnos(request):
    alumnos = Alumno.objects.all()
    dicc ={"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento= plantilla.render(dicc)
   
    return HttpResponse(documento)


def alta_alumnos(request):
    if request.method == "POST":

        mi_formulario = Alumno_formulario(request.POST)


        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
        alumnos = Alumno( nombre=datos['nombre'] , camada=datos['camada'])
        alumnos.save()
        
        return render(request , "alta_alumnos.html")

    return render(request , "alta_alumnos.html")  

def buscar_alumnos(request):
    
    return render(request , "buscar_alumnos.html")   
   
def busqueda_alumnos(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains = nombre)
        return render(request , "busqueda_alumnos.html" , {"alumnos": alumnos})
    else:
       return HttpResponse("Campo Vacio") 


#PROFESORES
def profesores(request):
    profesores = Profesor.objects.all()
    dicc ={"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento= plantilla.render(dicc)
   
    return HttpResponse(documento)


def alta_profesores(request):
    if request.method == "POST":

        mi_formulario = Profesor_formulario(request.POST)


        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
        profesores = Profesor( nombre=datos['nombre'] , legajo=datos['legajo'] , materia=datos['materia'])
        profesores.save()
        
        return render(request , "alta_profesores.html")

    return render(request , "alta_profesores.html")  

def buscar_profesores(request):
    
    return render(request , "buscar_profesores.html")   
   
def busqueda_profesores(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesores = Profesor.objects.filter(nombre__icontains = nombre)
        return render(request , "busqueda_profesores.html" , {"profesores": profesores})
    else:
       return HttpResponse("Campo Vacio")    