from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.


class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    ROLE_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Consultor', 'Consultor'),
    ]
    role = models.CharField(
        max_length=15, choices=ROLE_CHOICES, default="Consultor")


# Agrega related_name para evitar colisión de nombres

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(
        Permission, related_name='usuarios')

    def __str__(self):
        return self.username
