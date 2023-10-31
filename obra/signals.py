from django.db.models.signals import pre_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(pre_migrate)
def create_groups(sender, app_config, **kwargs):
    if app_config.name == 'tu_aplicacion':
        Group.objects.get_or_create(name='Administrador')
        Group.objects.get_or_create(name='Consultor')
