from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User


class SingUpForm(forms.Form):
    dni = forms.CharField(max_length=9, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu DNI'}))
    firstName = forms.CharField(label="Nombre", min_length=2, max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}))
    lastName = forms.CharField(label="Apellidos", min_length=2, max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu apellido'}))
    username = forms.CharField(label="Nombre del usuario", min_length=2, max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu usuario'}))
    telephone = forms.CharField(label="Teléfono", min_length=9, required=True)
    direction = forms.CharField(label="Dirección: ", min_length=2, max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu dirección'}))
    # bornDate = forms.DateField(required=True, widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'myDateClass', 'placeholder': 'dd-mm-YYYY'}))
    password = forms.CharField(label="Contraseña", min_length=2, max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repite la contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ya existe un usuario con ese nombre de usuario.')
        return username
    def clean_dni(self):
        dni=self.cleaned_data.get('dni')
        if User.objects.filter(dni=dni).exists():
            raise forms.ValidationError('Ya existe un usuario con ese dni.')
        return dni
    # def clean_bornDate(self):
    #     bornDate=self.cleaned_data.get('bornDate')
    #     if bornDate<=18:
    #         raise forms.ValidationError('Debes de ser mayor de 18 para crear un usuario aqui.')
    #     return bornDate
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden.')