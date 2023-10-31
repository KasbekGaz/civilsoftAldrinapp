from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsAdminUser, IsConsultorUser


class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserLoginView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = get_object_or_404(CustomUser, correo=request.data.get('correo'))
        if user.check_password(request.data.get('password')):
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Credenciales inválidas'}, status=401)


class UserLogoutView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        logout(request)
        return Response(status=204)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.user.rol == 'Consultor':
            return [IsConsultorUser()]
        elif self.request.user.rol == 'Administrador':
            return [IsAdminUser()]
        return []


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.user.rol == 'Consultor':
            return [IsConsultorUser()]
        elif self.request.user.rol == 'Administrador':
            return [IsAdminUser()]
        return []
