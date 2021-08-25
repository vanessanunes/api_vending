from datetime import datetime
from clients.models import Client
from sellers.models import Seller
from itens.models import Item
from django.db import models

class Cart(models.Model):
    
    class Meta:
        db_table = 'Cart'
        
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, null=True)
    itens = models.ManyToManyField(Item, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    commission = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.client)
    