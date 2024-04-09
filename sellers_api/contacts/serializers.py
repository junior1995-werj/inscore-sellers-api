from .models import SellerContactsModel, SellerGroupsModel
from rest_framework import serializers

DEFAULT_READ_ONLY_FIELDS = ("id", "updated_at")


class SellerContactsSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)

    class Meta:
        model = SellerContactsModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

    def create(self, validated_data):
        contact = SellerContactsModel.objects.create(**validated_data)
        return contact
    
class SellerGroupsSerializer(serializers.ModelSerializer):

    group_id = serializers.CharField(max_length=255)
    group_name = serializers.CharField(max_length=255)

    class Meta:
        model = SellerGroupsModel
        fields = '__all__'
        read_only_fields = DEFAULT_READ_ONLY_FIELDS

    def create(self, validated_data):
        contact = SellerGroupsModel.objects.create(**validated_data)
        return contact

class SellerContactNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerContactsModel
        fields = '__all__'

class SellerGroupNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerGroupsModel
        fields = '__all__'


