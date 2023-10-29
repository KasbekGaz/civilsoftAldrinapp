from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), many=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'groups')

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        if password1 != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        user = User.objects.create_user(**validated_data, password=password1)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError(
                "Por favor, ingrese el nombre de usuario y la contraseña.")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                "Credenciales incorrectas. Verifique su nombre de usuario y contraseña.")

        if not user.is_active:
            raise serializers.ValidationError(
                "Su cuenta está desactivada. Comuníquese con el administrador del sistema.")

        data['user'] = user
        return data
