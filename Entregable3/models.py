from django.db import models

# Los modelos seran, paciente, medico y turno
    
# class Turno(models.Model):
#     paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#     medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
#     fecha = models.DateField()
#     hora = models.TimeField()

    # def __str__(self):
    #     return self.paciente.nombre + " " + self.paciente.apellido + " - " + self.medico.nombre + " " + self.medico.apellido + " - " + str(self.fecha) + " - " + str(self.hora)