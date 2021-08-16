from sellers.models import Seller
from sellers.api.serializers import SellerSerializer
from rest_framework import viewsets

class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    
    def get_queryset(self):
        return Seller.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(SellerViewSet, self).list(request,  *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(SellerViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SellerViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(SellerViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(SellerViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(SellerViewSet, self).partial_update(request, *args, **kwargs)
    