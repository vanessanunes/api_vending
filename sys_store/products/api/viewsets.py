from products.models import Product
from products.api.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(ProductViewSet, self).list(request,  *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(ProductViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProductViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ProductViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ProductViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ProductViewSet, self).partial_update(request, *args, **kwargs)
    