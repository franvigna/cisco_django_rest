from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Se selecciona los campos que se desean agregar
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # campo solo de lectura que no se tiene que modificar
        read_only_fields = ('created_at',)
        