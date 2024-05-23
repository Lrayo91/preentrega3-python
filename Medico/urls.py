from django.urls import path
from Medico import views

app_name = 'medico'

urlpatterns = [

    path('', views.index, name='index'),
    path('nuevo/', views.new_medico, name='new_medico'),

    # path('medicos/', views.medicos),
    # path('new_medico/', views.new_medico),
    # path('listar_medicos/', views.listar_medicos),
]