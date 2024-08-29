from django.urls import path 
from . import views

appname = 'calcpeso'

urlpatterns = [
    path('', views.form,name='formulario' ),
]