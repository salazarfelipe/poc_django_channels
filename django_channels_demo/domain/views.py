from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny

from .models import Coordinates


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        fields = ('provider', 'latitude', 'longitude', 'created_at')


class CoordinatesAPIView(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    permission_classes = []
    authentication_classes = []
