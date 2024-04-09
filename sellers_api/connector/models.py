import uuid
from django.db import models
from seller.models import SellerModel

class ConnectorsModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=True) 
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        db_table = 'connector_connectors'

class SellerConnectorModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    connector_id = models.ForeignKey(ConnectorsModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=True) 
    connect_information = models.JSONField(null=False)

    class Meta:
        db_table = 'sellers_connectors'
