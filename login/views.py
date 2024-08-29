from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SueldoForm
from decimal import Decimal


# Credenciales correctas
USUARIO_CORRECTO = 'usuario_demo'
CONTRASEÑA_CORRECTA = 'contraseña_segura'

# Variable global para simular los intentos fallidos
intentos = 0

def login_view(request):
    global intentos

    if intentos >= 3:
        return HttpResponse("Has alcanzado el número máximo de intentos.")

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Lógica de verificación del usuario y contraseña
            if username == USUARIO_CORRECTO and password == CONTRASEÑA_CORRECTA:
                    intentos = 0  # Reinicia los intentos si el inicio de sesión es exitoso
                    return redirect('calculo_sueldo')
            else:
                intentos += 1
                intentos_restantes = 3 - intentos
                if intentos_restantes > 0:
                    return HttpResponse(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos_restantes}")
                else:
                    return HttpResponse("Has alcanzado el número máximo de intentos.")
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


def calculo_sueldo_view(request):
    if request.method == 'POST':
        form = SueldoForm(request.POST)
        if form.is_valid():
            # Datos básicos
            horas = Decimal(form.cleaned_data['horas_trabajadas'])
            tarifa = Decimal(form.cleaned_data['tarifa_por_hora'])
            hijos = form.cleaned_data['hijos']
            estado_civil = form.cleaned_data['estado_civil']

            # Sueldo básico
            sueldo_basico = horas * tarifa

            # Incremento por número de hijos
            if hijos <= 7:
                incremento_hijos = sueldo_basico * Decimal('0.10')
            else:
                incremento_hijos = sueldo_basico * Decimal('0.15')

            # Incremento por estado civil
            if estado_civil == 'casado':
                incremento_estado_civil = sueldo_basico * Decimal('0.02')
            else:  # soltero
                incremento_estado_civil = Decimal('100.00')

            # Asignación por hijos
            if hijos <= 4:
                asignacion_hijos = sueldo_basico * Decimal('0.01') * Decimal(hijos)
            else:
                asignacion_hijos = Decimal('500.00')

            # Sueldo total
            sueldo_total = sueldo_basico + incremento_hijos + incremento_estado_civil + asignacion_hijos

            return HttpResponse(f'El sueldo total es: {sueldo_total:.2f} soles')
    else:
        form = SueldoForm()

    return render(request, 'calculadora/calculo_sueldo.html', {'form': form})