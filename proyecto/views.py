from rest_framework import viewsets
from .models import Proyectos
from .serializers import ProyectosSerializer

# Create your views here.
class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectosSerializer