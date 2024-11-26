from django.shortcuts import render
from django.http import HttpResponse
from .forms import CursoForm,EstudianteForm,ProfesorForm
from .models import Curso

def inicio(req):
    return render(req, 'datosapp/index.html')

def cursos(req):
    return render(req, 'datosapp/cursos.html')

def profesores(req):
    return render(req, 'datosapp/profesores.html')

def estudiantes(req):
    return render(req, 'datosapp/estudiantes.html')


def agregar_curso(req):
    if req.method == 'POST':
        form = CursoForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'datosapp/agregar_curso.html')
    else:
        form = CursoForm()
    return render(req,'datosapp/agregar_curso.html', {'form': form})

def agregar_estudiante(req):
    if req.method == 'POST':
        form = EstudianteForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'datosapp/agregar_estudiante.html')
    else:
        form = EstudianteForm()
    return render(req, 'datosapp/agregar_estudiante.html', {'form': form})

def agregar_profesor(req):
    if req.method == 'POST':
        form = ProfesorForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req,'datosapp/agregar_profesor.html')
    else:
        form = ProfesorForm()
    return render(req, 'datosapp/agregar_profesor.html', {'form': form})



def busqueda_camada(req):
    return render(req,'datosapp/busqueda_camada.html')

def buscar(req):
    if req.GET['camada']:
        camada = req.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(req,'datosapp/resultados_busqueda.html' , {'cursos':cursos, 'camada':camada})
    else:
        respuesta = 'No enviaste datos'
    return HttpResponse(respuesta)