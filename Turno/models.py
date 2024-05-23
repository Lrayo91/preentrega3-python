from django.db import models

# Turno tiene el mail de un paciente, la matricula de un médico, la fecha y hora del turno

class Turno(models.Model):
    mailPaciente = models.EmailField()
    matriculaMedico = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.mailPaciente} - {self.matriculaMedico} - {self.fecha} - {self.hora}'