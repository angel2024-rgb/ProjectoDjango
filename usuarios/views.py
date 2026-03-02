from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegistroSerializer, UsuarioSerializer

class RegistroView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response({
                'mensaje': 'Usuario registrado exitosamente',
                'usuario': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

""" class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        
        username = request.data.get("username")
        password = request.data.get("password")
        
        
        if not username or not password:
            return Response({
                'error': 'Debe proporcionar username y password'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        
        user = authenticate(username=username, password=password)
        
        
        if user:
            login(request, user)
            serializer = UsuarioSerializer(user)  
            return Response({
                'mensaje': 'Login exitoso',
                'usuario': serializer.data
            }, status=status.HTTP_200_OK) 
        else:
            return Response({
                'error': 'Credenciales inválidas'
            }, status=status.HTTP_401_UNAUTHORIZED)  """ 


class PerfilView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        usuario = request.user
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)


""" class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({
            'mensaje': 'Sesión cerrada exitosamente'
        }, status=status.HTTP_200_OK) """