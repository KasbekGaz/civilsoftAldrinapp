from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import Usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required  # *para proteger las rutas
# Create your views here.


# ! Pagina de home, para el usuario que inicia sesion


def home(request):
    return render(request, 'home.html')

# ! Pagina de informacion, pagina para el usuario no registrado y no autenticado


def about(request):
    return render(request, 'about.html')

# ! registro de usuario


def new_usuario(request):
    if request.method == 'GET':
        return render(request, 'registro_Usuario.html', {
            'form': Usuario
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:  # * Aqui se registra el usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro_Usuario.html', {
                    'form': Usuario,
                    'error': 'Usuario no existe'
                })
        return render(request, 'registro_Usuario.html')


#! Autenticar e incio de sesion del usuario
def autenticar(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:  # Si el usuario no existe
            return render(request, 'inicio_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:  # si SI existe lo reenvia a TASKS
            login(request, user)
            return redirect('home')


#! Cerrar sesion usuario
@login_required
def closeSesion(request):
    logout(request)
    return redirect('home')
