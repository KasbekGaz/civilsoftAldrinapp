from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import Usuario
from django.contrib.auth import login, logout
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
# * modififcado


def new_usuario(request):
    if request.method == 'GET':
        return render(request, 'registro_Usuario.html', {
            'form': Usuario()
        })
    elif request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Esto crea un nuevo usuario y un perfil asociado
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro_Usuario.html', {
                    'form': form,
                    'error': 'Usuario ya existe'
                })
    return render(request, 'registro_Usuario.html', {'form': Usuario()})


#! Autenticar e incio de sesion del usuario
# * modificado
def autenticar(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form': AuthenticationForm()
        })
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'inicio_sesion.html', {
            'form': form,
            'error': 'Usuario o contraseña incorrecta'
        })


#! Cerrar sesion usuario
@login_required
def closeSesion(request):
    logout(request)
    return redirect('home')
