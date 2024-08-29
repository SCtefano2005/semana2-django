from django.urls import path
from .views import login_view, calculo_sueldo_view

urlpatterns = [
    path('', login_view, name='login'),
    path('calculo_sueldo/', calculo_sueldo_view, name='calculo_sueldo'),
]
