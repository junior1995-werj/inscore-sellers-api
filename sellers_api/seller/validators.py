from validate_docbr import CNPJ
from rest_framework.exceptions import ValidationError
from .models import SellerModel, UserModel

def validate_cnpj(value):
    cnpj_validator = CNPJ()
    if not cnpj_validator.validate(value):
        raise ValidationError("SellerAPI error: CPNJ invalid")
    if SellerModel.objects.filter(cnpj=value).exists():
        raise ValidationError("SellerAPI error: CPNJ already exists in the database")

def validate_email(value):
    if UserModel.objects.filter(email=value).exists():
        raise ValidationError("SellerAPI error: email already exists in the database")
    
def validate_name(value):
    if SellerModel.objects.filter(name=value).exists():
        raise ValidationError("SellerAPI error: name already exists in the database")
    
def validate_username(value):
    if UserModel.objects.filter(username=value).exists():
        raise ValidationError("SellerAPI error: username already exists in the database")
    