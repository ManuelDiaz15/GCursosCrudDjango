from django.shortcuts import render, redirect
from .models import Curso # Se importa el modelo creado anterioremente
# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()#Se crea una variable curso
    return render(request, "gestionCursos.html", {"cursos": cursosListados})#De esta forma se envia "cursos" a la plantilla, este es una lista creada desde models

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')

def eliminarCurso(request, codigo):  #El codigo hace referencia a el curso al cual se desea eliminar
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')#Redirige a la raiz 