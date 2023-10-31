from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    nombre_completo = models.CharField(max_length=100, null=True)
    groups = models.ManyToManyField(
        Group, blank=True, verbose_name='Grupos del Usuario')
    correo = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Correo Electronico')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
