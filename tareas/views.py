from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tarea
from .serializers import TareaSerializer
from django.shortcuts import render

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    @action(detail=False, methods=['get'])
    def pendientes(self, request):
        tareas = self.get_queryset().filter(completada=False)
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def completadas(self, request):
        tareas = self.get_queryset().filter(completada=True)
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def marcar_completada(self, request, pk=None):
        """
        Marca una tarea específica como completada
        """
        tarea = self.get_object()  # Obtiene la tarea con el ID (pk)
        tarea.completada = True
        tarea.save()
        return Response({'mensaje': 'Tarea marcada como completada'}, 
                        status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def marcar_pendiente(self, request, pk=None):
        """
        Marca una tarea específica como pendiente
        """
        tarea = self.get_object()
        tarea.completada = False
        tarea.save()
        return Response({'mensaje': 'Tarea marcada como pendiente'}, 
                        status=status.HTTP_200_OK)
    
def frontend(request):
    return render(request, 'index.html')