from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Tarea
from .serializers import TareaSerializer
from django.shortcuts import get_object_or_404

class TareaListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        tareas = Tarea.objects.filter(usuario=request.user)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response({
                'mensaje': 'Tarea creada exitosamente',
                'tarea': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class TareaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        serializer = TareaSerializer(tarea)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        serializer = TareaSerializer(tarea, data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response({
                'mensaje': 'Tarea actualizada exitosamente',
                'tarea': serializer.data
            }, status=status.HTTP_200_OK)  
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TareaPendientesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        tareas = Tarea.objects.filter(usuario=request.user, completada = False)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TareaCompletadasView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        tareas = Tarea.objects.filter(usuario=request.user, completada = True)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TareaMarcarCompletadaView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        tarea.completada = True
        tarea.save()
        
        serializer = TareaSerializer(tarea)
        return Response({
            'mensaje': 'Tarea marcada como completada',
            'tarea': serializer.data
        }, status=status.HTTP_200_OK)

    
class TareaMarcarPendienteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
        tarea.completada = False
        tarea.save()
        
        serializer = TareaSerializer(tarea)
        return Response({
            'mensaje': 'Tarea marcada como pendiente',
            'tarea': serializer.data
        }, status=status.HTTP_200_OK)

