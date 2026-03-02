from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'completada', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']