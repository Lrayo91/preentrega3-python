# paciente/urls.py

from django.urls import path
from Paciente import views

app_name = 'paciente'

urlpatterns = [

    path('', views.index, name='index'),
    path('new_paciente/', views.new_paciente, name='new_paciente'),
    path('buscar_paciente/', views.buscar_paciente, name='buscar_paciente'),
    path('buscar_paciente_resultado/', views.buscar_paciente_resultado, name='buscar_paciente_resultado'),

]