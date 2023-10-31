from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Usuario(UserCreationForm):
    nombre_completo = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = Profile
        fields = ('nombre_completo', 'email', 'password1', 'password2')

# *Nos lo dio chatgpt
    def save(self, commit=True):
        user = super(Usuario, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user, nombre_completo=self.cleaned_data['nombre_completo'])
        return user
