from django.db import models

# Los modelos seran, paciente, medico y turno

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido
    
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellido
    
class Turno(models.Model):
    mailPaciente = models.EmailField()
    matriculaMedico = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.mailPaciente} - {self.matriculaMedico} - {self.fecha} - {self.hora}'