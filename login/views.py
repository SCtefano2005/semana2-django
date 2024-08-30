from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SueldoForm
user = 'Stefano'
contra = '123456789'

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

            
            if username == user and password == contra:
                    intentos = 0  
                    return redirect('calculo_sueldo')
            else:
                intentos += 1
                intentos_restantes = 3 - intentos
                if intentos_restantes > 0:
                    return render(request, 'login/login.html', {
                        'form': LoginForm(),
                        'error': f'Credenciales incorrectas. Te quedan {intentos_restantes} intentos restantes.'
                        
                    })
                else:
                    return render(request, 'login/login.html', {
                        'form': LoginForm(),
                        'error': 'Has alcanzado el numero maximo de intentos :c',
                        'form_disabled': True,
                    })
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def calculo_sueldo_view(request):
    if request.method == 'POST':
        form = SueldoForm(request.POST)
        if form.is_valid():
            horas = float(form.cleaned_data['horas_trabajadas'])
            tarifa = float(form.cleaned_data['tarifa_por_hora'])
            hijos = form.cleaned_data['hijos']
            estado_civil = form.cleaned_data['estado_civil']
            
            sueldo_basico = horas * tarifa
            if hijos <= 7:
                incremento_hijos = sueldo_basico * 0.10
            else:
                incremento_hijos = sueldo_basico * 0.15
            if estado_civil == 'casado':
                incremento_estado_civil = sueldo_basico * 0.02
            else:  
                incremento_estado_civil = 100.00
            if hijos <= 4:
                asignacion_hijos = sueldo_basico * 0.01 * hijos
            else:
                asignacion_hijos = 500.00

            sueldo_total = sueldo_basico + incremento_hijos + incremento_estado_civil + asignacion_hijos

            return HttpResponse(f'El sueldo total es: {sueldo_total:.2f} soles')
    else:
        form = SueldoForm()

    return render(request, 'calculadora/calculo_sueldo.html', {'form': form})