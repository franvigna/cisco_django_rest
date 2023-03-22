from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    # que consultas se van a poder hacer
    # consulta todos los datos de una tabla
    queryset = Project.objects.all()
    # se declara el tipo de permiso
    permission_classes = [permissions.AllowAny]
    # que serializer utiliza 
    serializer_class = ProjectSerializer