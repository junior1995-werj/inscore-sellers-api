from .models import SellerModel, UserModel, UserAuthModel
from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q
from .validators import (
    validate_cnpj, 
    validate_name, 
    validate_email, 
    validate_username
)

DEFAULT_READ_ONLY_FIELDS = ("id", "updated_at")

class SellerSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=20)
    cnpj = serializers.CharField(max_length=30, validators=[validate_cnpj])
    email = serializers.CharField(max_length=100)

    class Meta:
        model = SellerModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS


    def create(self, validated_data):
        validate_name(validated_data['email'])
        seller = SellerModel.objects.create(**validated_data)
        return seller
    
    def update(self, instance, validated_data):
        if instance.name != validated_data['name']:
            validate_name(validated_data['name'])
        return super().update(instance, validated_data)
    
class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    status = serializers.BooleanField(default=True) 
    email = serializers.CharField(max_length=100)

    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

    def create(self, validated_data):
        validate_username(validated_data['username'])
        user = UserModel.objects.create(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        if instance.username != validated_data['username']:
            validate_username(validated_data['username'])
        return super().update(instance, validated_data)
    
class UserSellerIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'
