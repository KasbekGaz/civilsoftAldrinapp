from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsMemberOfGroup
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics


# ! Pagina de home, para el usuario que inicia sesion
def home(request):
    return render(request, 'home.html')


# ! Pagina de informacion, pagina para el usuario no registrado y no autenticado
def about(request):
    return render(request, 'about.html')


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        return [IsMemberOfGroup()]

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser])
    def registrar_usuario(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#! registrar usuario
class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # *Permite a cualquiera registrarse


#! login
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

#! logout


class LogoutView(APIView):
    def post(self, request):
        request.auth.delete()  # Elimina el token de autenticación del usuario
        return Response(status=status.HTTP_200_OK)
