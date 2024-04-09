from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import SellerModel
from .actions import ValidateSellerPreCreate

@receiver(pre_save, sender=SellerModel)
def pre_save_actions(sender, instance, created, **kwargs):
    if created:
        ValidateSellerPreCreate(instance)

@receiver(post_save, sender=SellerModel)
def post_save_actions(sender, instance, created, **kwargs):
    if created:
        # Realize a ação personalizada aqui
        print("ok")