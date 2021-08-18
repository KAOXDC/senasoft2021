from django import forms
from .models import Auto, Marca

class agregar_auto_form (forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        #exclude = ['foto']

class agregar_marca_form (forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        #exclude = ['foto']

class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput()) # input TEXT html
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False)) # input PASSWROD html