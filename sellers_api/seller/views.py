from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from .models import SellerModel, UserModel
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from .serializers import SellerSerializer, UserSerializer, UserSellerIDSerializer
from django_filters.rest_framework import DjangoFilterBackend
import bcrypt
import cryptocode
from sellers_api.settings import KEY_PASS



class SellerViewSet(viewsets.ModelViewSet):
    http_method_names = ("get", "post", "patch")
    queryset = SellerModel.objects.all().order_by('-created_at')
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller_id', 'status', 'username']
    permission_classes = [permissions.IsAuthenticated]

class UserSellerIDViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, seller_id=None, username=None):
        if username:
            queryset = UserModel.objects.filter(Q(seller_id=seller_id, username=username)).first()
        else: 
            queryset = UserModel.objects.filter(seller_id=seller_id)
        if not queryset:
            return Response({'Sellers API': 'User not found'}, status=404)
        serializer = UserSellerIDSerializer(queryset.all(), many=True)
        return Response(serializer.data)
    
class SellerAuthViewSet(APIView):
    http_method_names = ("post", "options")
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        queryset = UserModel.objects.filter(Q(username=request.data['username'], status=True)).first()
        if not queryset:
            return Response({'Sellers API': 'User não encontrado'}, status=404)   
        
        pass_db = cryptocode.decrypt(queryset.password, KEY_PASS)

        if pass_db == request.data['password']:
            return Response({"seller_id": queryset.seller_id.id, "username": queryset.username}, status=status.HTTP_200_OK)

        return Response({'Sellers API': 'User e senha incorretos'}, status=200)
        
