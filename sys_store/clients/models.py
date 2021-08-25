from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Client'
    
    def __str__(self):
        return self.name
