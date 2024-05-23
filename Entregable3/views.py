from django.http import HttpResponse
from django.template import Template, Context, loader

def index(request):
    
    plantilla = loader.get_template("Entregable3/index.html")

    documento = plantilla.render()

    return HttpResponse(documento)
