from products.models import Product
from django.db import models

class Item(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    
    readonly_fields = ('price')
    
    def __str__(self):
        return str(self.product)
    
    def save(self, *args, **kwargs):
        if self.product:
            self.price = self.quantity*self.product.price
        super(Item, self).save(*args, **kwargs)
        