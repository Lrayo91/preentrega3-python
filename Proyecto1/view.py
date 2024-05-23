from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola mundo")

def probando_template(self):
    # mi_template = open("Proyecto1/Proyecto1/templates/template1.html")
    
    # plantilla = Template(mi_template.read())

    # mi_template.close()

    # contexto = Context()

    # documento = plantilla.render(contexto)

    diccionario = {"nombre_persona": "Juan", "apellido_persona": "Perez"}   

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)