from .serializer import PerfumesSerializer
from .models import Perfumes
from rest_framework import viewsets

class PerfumesView(viewsets.ModelViewSet):
    serializer_class=PerfumesSerializer
    queryset=Perfumes.objects.all()