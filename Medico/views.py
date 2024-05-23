from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Medico
from .forms import MedicoForm

def index(request):
    medicos = Medico.objects.all()
    contexto = {
        'medicos': medicos
    }

    plantilla = loader.get_template("Medico/index.html")
    documento = plantilla.render(contexto, request)

    return HttpResponse(documento)

def new_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico:index')
    else:
        form = MedicoForm()

    contexto = {
        'form': form
    }

    return render(request, 'Medico/new_medico.html', contexto)
