from .models import Project
from rest_framework import permissions, viewsets
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    prermission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
