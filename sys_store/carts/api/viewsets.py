from carts.models import Cart
from carts.api.serializers import CartSerializer
from rest_framework import viewsets

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    
    def get_queryset(self):
        return Cart.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(CartViewSet, self).list(request,  *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(CartViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CartViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CartViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CartViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CartViewSet, self).partial_update(request, *args, **kwargs)
    