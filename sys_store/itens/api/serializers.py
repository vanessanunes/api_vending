from products.models import Product
from products.api.serializers import ProductSerializer
from itens.models import Item
from rest_framework.serializers import ModelSerializer

class ItemSerializer(ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = Item
        fields = '__all__'
        
    def create(self, validated_data):
        product = validated_data['product']
        del validated_data['product']
        validated_data['product'] = self.create_product(product)
        item = Item.objects.create(**validated_data)
        return item
    
    def create_product(self, products):
        return Product.objects.create(**products)
    