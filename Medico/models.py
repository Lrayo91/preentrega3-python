from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)    # la matrícula debe ser única

    def __str__(self):
        return self.nombre + " " + self.apellido
