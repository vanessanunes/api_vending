from itens.models import Item
from itens.api.serializers import ItemSerializer
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(ItemViewSet, self).list(request,  *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(ItemViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ItemViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ItemViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ItemViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ItemViewSet, self).partial_update(request, *args, **kwargs)
    