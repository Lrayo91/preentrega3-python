# paciente/models.py

from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True) # el correo debe ser único

    def __str__(self):
        return self.nombre + " " + self.apellido