from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Resto de tu código en forms.py


class Usuario(UserCreationForm):
    nombre_completo = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('nombre_completo', 'email')
