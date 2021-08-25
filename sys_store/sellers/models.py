from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Seller'
    
    def __str__(self):
        return self.name
