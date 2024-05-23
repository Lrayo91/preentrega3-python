from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Turno
from .forms import TurnoForm

def index(request):
    turnos = Turno.objects.all()
    contexto = {
        'turnos': turnos
    }

    plantilla = loader.get_template("Turno/index.html")
    documento = plantilla.render(contexto, request)

    return HttpResponse(documento)

def new_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('turno:index')
    else:
        form = TurnoForm()

    return render(request, 'Turno/new_turno.html', {'form': form})
