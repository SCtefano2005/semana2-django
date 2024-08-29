from django.shortcuts import render

def index(request):
    context = {
        'titulo' : 'Formulario',
    }
    
    return render(request, 'encuestas/form.html', context)

def enviar(request):
    context = {
        'titulo' : 'Respuesta',
        'nombre' : request.POST['nombre'],
        'password' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiosmas': request.POST.getlist('idiomas'),
        'email' : request.POST['email'],
        'website' : request.POST.get('website'),
    }
    return render(request, 'encuestas/respuesta.html', context)