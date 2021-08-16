from datetime import datetime
from clients.models import Client
from sellers.models import Seller
from itens.models import Item
from django.db import models

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    datetime = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.client)
    
    def save(self, *args, **kwargs):
        # super_query = super(Cart, self).get_queryset()
        super(Cart, self).save(*args, **kwargs)
        # import pdb ; pdb.set_trace()
        
        amount = 0
        self.total_value = 0
        
        for value in self.itens.values(): 
            amount += value.get('price')
                    
        self.total_value = amount
        
        current_time = self.datetime.strftime("%H:%M:%S")
        current_time = datetime.strptime(current_time, '%H:%M:%S')
        first_day = datetime.strptime('00:00:00', '%H:%M:%S')
        second_day = datetime.strptime('12:00:00', '%H:%M:%S')
        if current_time > first_day and current_time < second_day:
            commission = 5/100
        else:
            commission = 4/100
        self.commission = commission*float(self.total_value)
        
        super(Cart, self).save(*args, **kwargs)