from carts.models import Cart
from rest_framework.serializers import ModelSerializer

class CartSerializer(ModelSerializer):
    
    class Meta:
        model = Cart
        fields = '__all__'
        
    