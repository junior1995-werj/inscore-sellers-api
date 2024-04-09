from .models import ConnectorsModel, SellerConnectorModel
from rest_framework import serializers

DEFAULT_READ_ONLY_FIELDS = ("id", "updated_at")

class ConnetorsSerializer(serializers.ModelSerializer): 

    name = serializers.CharField(max_length=255)

    class Meta:
        model = ConnectorsModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

class SellerConnectorsSerializer(serializers.ModelSerializer):

    connect_information = serializers.JSONField()

    class Meta:
        model = SellerConnectorModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

