# turno/urls.py

from django.urls import path
from Turno import views

app_name = 'turno'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('new_turno/', views.new_turno, name='new_turno'),
    
]