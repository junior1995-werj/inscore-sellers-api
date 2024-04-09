from rest_framework import permissions, viewsets
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SellerGroupsModel, SellerContactsModel
from .serializers import SellerContactsSerializer, SellerGroupsSerializer, SellerContactNameSerializer, SellerGroupNameSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .handler import send_message_sqs
from rest_framework import status

class SellerContactsViewSet(viewsets.ModelViewSet):

    http_method_names = ("get", "post", "patch")
    serializer_class = SellerContactsSerializer
    queryset = SellerContactsModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id', 'name', 'phone_number']
    permission_classes = [permissions.IsAuthenticated]

class SellerGruopsViewSet(viewsets.ModelViewSet):

    http_method_names = ("get", "post", "patch")
    serializer_class = SellerGroupsSerializer
    queryset = SellerGroupsModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id', 'group_id', 'group_name']
    permission_classes = [permissions.IsAuthenticated]

class SellerContactNameViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, id=None, name=None):
        if name:
            queryset = SellerContactsModel.objects.filter(Q(seller_id=id) and Q(name=name)).first()
        else: 
            queryset = SellerContactsModel.objects.filter(seller_id=id)
        if not queryset:
            return Response({'Sellers API': 'Seller contact not found'}, status=404)
        serializer = SellerContactNameSerializer(queryset, many=True)
        return Response(serializer.data)

class SellerGroupNameViewSet(viewsets.ViewSet):
    
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, id=None, name=None):
        if name:
            queryset = SellerGroupsModel.objects.filter(Q(seller_id=id, group_name=name)).first()
        else: 
            queryset = SellerGroupsModel.objects.filter(seller_id=id)
        if not queryset:
            return Response({'Sellers API': 'Seller contact not found'}, status=404)
        serializer = SellerGroupNameSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SincGroupsViewSet(APIView):
    http_method_names = ("post", "options")
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Iniciar o processamento assíncrono em uma função separada
        send_message_sqs(request.data['seller_id'])
        return Response({"message": "Processamento iniciado"}, status=status.HTTP_202_ACCEPTED)
    
