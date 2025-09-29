from rest_framework import serializers
from .models import Perfumes

class PerfumesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perfumes
        fields='__all__'