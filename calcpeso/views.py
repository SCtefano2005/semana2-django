from django.shortcuts import render
from datetime import date
def calculo(cumpleaños):
    presente = date.today()
    edad = presente.year - cumpleaños.year - ((presente.month, presente.day) < (cumpleaños.month, cumpleaños.day))
    # resta el presente, cumpleaños y por ultimo puse un booleando que compara la fecha actual y la fecha cumple,
    # si la fecha actual es anterior de la fecha de cumpleaños en formato mes/dia devolvera true osea 1 y si es igual o posterior
    # devolvera false osea 0
    signos_zodiaco = [
    ('Capricornio', (1, 19)), 
    ('Acuario', (2, 18)),      
    ('Piscis', (3, 20)),     
    ('Aries', (4, 19)),       
    ('Tauro', (5, 20)),        
    ('Géminis', (6, 20)),   
    ('Cáncer', (7, 22)),      
    ('Leo', (8, 22)),     
    ('Virgo', (9, 22)),        
    ('Libra', (10, 22)),      
    ('Escorpio', (11, 21)),    
    ('Sagitario', (12, 21)),   
    ('Capricornio', (12, 31))  
    ]
    
    def buscar(index=0):
        sign, (month, day) = signos_zodiaco[index]
        C_M_D = (cumpleaños.month, cumpleaños.day)
        
        if C_M_D <= (month, day) and (index == 0 or C_M_D > signos_zodiaco[index - 1][1]):
            return sign
        elif index < len(signos_zodiaco) - 1:
            return buscar(index + 1)
        else:
            return 'Capricornio'
              
    signo_zodiaco = buscar()
    return edad, signo_zodiaco

def form(request):
    if request.method == 'POST':
        cumple_string = request.POST.get('birthdate')
        cumple = date.fromisoformat(cumple_string)
        edad, signo_zodiaco = calculo(cumple)

        context = {
            'edad': edad,
            'signozodiac': signo_zodiaco,
        }
        return render(request, 'formulario/formulario.html', context)
    return render(request, 'formulario/formulario.html')
