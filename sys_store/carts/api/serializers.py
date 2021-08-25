# from products.models import Product
from sellers.models import Seller
from sellers.api.serializers import SellerSerializer
from products.models import Product
from itens.api.serializers import ItemSerializer
from itens.models import Item
from clients.models import Client
from clients.api.serializers import ClientSerializer
from carts.models import Cart
from rest_framework.serializers import ModelSerializer

class CartSerializer(ModelSerializer):
    client = ClientSerializer()
    seller = SellerSerializer()
    itens = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


    def calculate_commission(self, cart):

        current_time = cart.datetime.strftime("%H:%M:%S")
        current_time = cart.datetime.strptime(current_time, '%H:%M:%S')
        first_day = cart.datetime.strptime('00:00:00', '%H:%M:%S')
        second_day = cart.datetime.strptime('12:00:00', '%H:%M:%S')

        commission = 0

        if current_time > first_day and current_time < second_day:
            commission = 5/100
        else:
            commission = 4/100

        return commission

    def return_total_value(self, itens):

        total_value = 0

        for item in itens:
            total_value += item['product'].price * item['quantity']

        return total_value

    def create_itens(self, itens, cart):

        for item in itens:
            product = item.get('product')

            product_instance = Product.objects.get_or_create(**product)

            item['product'] = product_instance[0]
            item_instance = Item.objects.create(**item)

            cart.itens.add(item_instance)

    def create(self, validated_data):

        itens = validated_data['itens']
        del validated_data['itens']

        client = validated_data['client']
        del validated_data['client']

        seller = validated_data['seller']
        del validated_data['seller']

        client_instance = Client.objects.get_or_create(**client)[0]

        seller_instance = Seller.objects.get_or_create(**seller)[0]

        cart = Cart.objects.create(**validated_data)

        item_instance = self.create_itens(itens, cart)

        cart.client = client_instance
        cart.seller = seller_instance
        cart.total_value = self.return_total_value(itens)

        commission = self.calculate_commission(cart)

        cart.commission = commission*float(cart.total_value)

        cart.save()

        return cart
