from rest_framework import permissions, viewsets
from .models import ConnectorsModel, SellerConnectorModel
from .serializers import ConnetorsSerializer, SellerConnectorsSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ConnetorsViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post")
    queryset = ConnectorsModel.objects.all().order_by('-updated_at')
    serializer_class = ConnetorsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SellerConnectorsViewSet(viewsets.ModelViewSet):

    serializer_class = SellerConnectorsSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = SellerConnectorModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id', 'status', 'connector_id']
    permission_classes = [permissions.IsAuthenticated]