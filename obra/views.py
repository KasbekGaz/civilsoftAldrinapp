from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import Usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required  # *para proteger las rutas
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
# Create your views here.

# ! Pagina de home, para el usuario que inicia sesion


def home(request):
    return render(request, 'home.html')

# ! Pagina de informacion, pagina para el usuario no registrado y no autenticado


def about(request):
    return render(request, 'about.html')

# ! registro de usuario


def new_usuario(request):
    if request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            user = form.save()
            # Obtén el grupo seleccionado
            group_name = request.POST.get('group')
            if group_name == 'Administrador':
                # Obtén el grupo "Administrador"
                admin_group = Group.objects.get(name='Administrador')
                user.groups.add(admin_group)
            elif group_name == 'Consultor':
                consultor_group = Group.objects.get(
                    name='Consultor')  # Obtén el grupo "Consultor"
                user.groups.add(consultor_group)
            login(request, user)
            return redirect('home')
        else:
            # Manejar errores de validación del formulario
            # Puedes mostrar mensajes de error en el formulario
            return render(request, 'registro_Usuario.html', {'form': form})
    else:
        form = Usuario()
    return render(request, 'registro_Usuario.html', {'form': form})


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
