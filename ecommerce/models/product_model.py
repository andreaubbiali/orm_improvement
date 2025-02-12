from django.db import models
from .product_type import ProductType

class Product(models.Model):

    def __init__(self, username=None, email=None, password=None, phone=None, address=None, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent constructor
        self.type = models.ForeignKey(ProductType, on_delete=models.PROTECT, on_update=models.CASCADE, to_field='id')
    
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
