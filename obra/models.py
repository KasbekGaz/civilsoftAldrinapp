from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

# Agrega related_name para evitar colisión de nombres
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        related_query_name='usuario_group'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_user_permissions',
        related_query_name='usuario_user_permission'
    )

    def __str__(self):
        return self.nombre_completo
