from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('Administrador', 'Administrador'),
        ('Consultor', 'Consultor'),
    )

    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES)
    # Define un related_name personalizado para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='Groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='User permissions'
    )

    def __str__(self):
        return self.username
