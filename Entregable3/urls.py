from django.urls import path
from Entregable3 import views

app_name = 'Entregable3'

urlpatterns = [

    path('', views.index, name='index'),

]