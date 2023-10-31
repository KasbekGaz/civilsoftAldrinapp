from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.models import Group, Permission


class UsuarioSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), many=True, required=False)
    user_permissions = serializers.SlugRelatedField(
        slug_field='codename', queryset=Permission.objects.all(), many=True, required=False)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre_completo', 'telefono',
                  'correo', 'groups', 'user_permissions']
