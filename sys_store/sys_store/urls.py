"""sys_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from carts.api.viewsets import CartViewSet
from itens.api.viewsets import ItemViewSet
from products.api.viewsets import ProductViewSet
from clients.api.viewsets import ClientViewSet
from sellers.api.viewsets import SellerViewSet
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'sellers', SellerViewSet, basename='Seller')
router.register(r'clients', ClientViewSet, basename='Client')
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'itens', ItemViewSet, basename='Item')
router.register(r'carts', CartViewSet, basename='Cart')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
