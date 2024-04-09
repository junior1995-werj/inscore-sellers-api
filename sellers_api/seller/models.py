import uuid
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime
import cryptocode
from sellers_api.settings import KEY_PASS

class SellerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    status = models.BooleanField(default=True) 
    plan_id = models.UUIDField(null=True)
    cnpj = models.CharField(max_length=30)
    created_at = models.DateTimeField(null=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    complement = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=2550, null=True)

    class Meta:
        db_table = 'sellers_seller'

    def __str__(self):
        return f"seller_id={self.id}, name={self.name}, status={self.status}"

@receiver(post_save, sender=SellerModel, dispatch_uid="card_proative_config_model_post_save")
def create_event_message_post_save(sender, instance, created, **kwargs):
    if created:
        instance = SellerModel.objects.filter(name=instance.name).first()
        
        if not UserModel.objects.filter(seller_id=instance.id).exists():
            data = {
                "seller_id" : instance,
                "email" : instance.email,
                "username" : instance.email,
                "password" : instance.password,
                "created_at" : datetime.now()
            }
            UserModel.objects.create(**data)
            
class UserModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(null=False, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'sellers_user'
    
    def __str__(self):
        return f"seller_id={self.id}, name={self.username}, status={self.status}, email={self.email}"
    

@receiver(pre_save, sender=UserModel)
def pre_save_user(sender, instance, **kwargs): 
    
    if not cryptocode.decrypt(instance.password, KEY_PASS):
        instance.password = cryptocode.encrypt(instance.password, KEY_PASS)
    else: 
        pass

class UserAuthModel(models.Model):
    username = models.CharField(max_length=255)
    seller_id = models.CharField(max_length=255,null=True)