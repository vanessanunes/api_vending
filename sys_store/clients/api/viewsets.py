from clients.models import Client
from clients.api.serializers import ClientSerializer
from rest_framework import viewsets

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        return Client.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(ClientViewSet, self).list(request,  *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(ClientViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ClientViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ClientViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ClientViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ClientViewSet, self).partial_update(request, *args, **kwargs)
    