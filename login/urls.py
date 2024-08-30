from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('calculo_sueldo/', calculo_sueldo_view, name='calculo_sueldo'),
]
