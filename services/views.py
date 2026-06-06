from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'
