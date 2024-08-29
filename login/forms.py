from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class SueldoForm(forms.Form):
    horas_trabajadas = forms.IntegerField(label='Horas trabajadas')
    tarifa_por_hora = forms.DecimalField(max_digits=10, decimal_places=2, label='Tarifa por hora')
    hijos = forms.IntegerField(label='Número de hijos', min_value=0)
    estado_civil = forms.ChoiceField(choices=[('casado', 'Casado'), ('soltero', 'Soltero')], label='Estado civil')
