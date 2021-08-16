from products.models import Product
from products.api.serializers import ProductSerializer
from itens.models import Item
from rest_framework.serializers import ModelSerializer

class ItemSerializer(ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = Item
        fields = '__all__'
        
    # def create(self, validated_data):
    #     print(validated_data)
    #     product = validated_data['product']
    #     del validated_data['product']
    #     itens = 
    #     import pdb ; pdb.set_trace()
    #     # item = Item.objects.get(id=1)
    #     # Product.objects.filter(id=validated_data.)
    #     import pdb ; pdb.set_trace()
        
        
    