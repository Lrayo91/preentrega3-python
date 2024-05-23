from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Paciente
from .forms import PacienteForm

def index(request):
    pacientes = Paciente.objects.all()
    contexto = {
        'pacientes': pacientes
    }

    plantilla = loader.get_template("Paciente/index.html")
    documento = plantilla.render(contexto, request)

    return HttpResponse(documento)

def new_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('paciente:index')
    else:
        form = PacienteForm()

    return render(request, 'Paciente/new_paciente.html', {'form': form})

def buscar_paciente(request):

    return render(request, 'Paciente/buscar_paciente.html')

def buscar_paciente_resultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        pacientes = Paciente.objects.filter(nombre=request.GET["nombre"].capitalize())  # Pongo el nombre en mayusculas para que no haya problemas con la busqueda (si el nombre esta en la base de datos en minusculas y el usuario lo introduce en mayusculas no lo encontrara

        return render(request, 'Paciente/buscar_paciente_resultado.html', {'pacientes': pacientes})
    
    else:
        respuesta = "No has introducido ningun nombre"

    return HttpResponse(respuesta)

