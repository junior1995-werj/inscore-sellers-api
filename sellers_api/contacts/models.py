import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .actions import send_message_sqs

from seller.models import SellerModel

class SellerContactsModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.BooleanField(default=True) 
    
    class Meta:
        db_table = 'sellers_contacts'

    def __str__(self):
        return f"seller_id={self.id}, name={self.name}, status={self.phone_number}"

class SellerGroupsModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.BooleanField(default=True) 
    contacts_group = models.JSONField(null=True)
    description = models.CharField(max_length=255, null=True)
    restrict = models.BooleanField(null=True) 

    class Meta:
        db_table = 'sellers_groups'

@receiver(post_save, sender=SellerGroupsModel, dispatch_uid="create_group_post_save_post_save")
def create_group_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.group_id == "0":
            send_message_sqs(instance)
        
