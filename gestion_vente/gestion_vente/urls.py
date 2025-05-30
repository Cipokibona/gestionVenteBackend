"""
URL configuration for gestion_vente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from gestion.views import UserAPIView, TypeEchangeView, WalletView, TauxEchangeView, TransactionsView, BasketListView, BasketForAgentView, CustomerView, VenteView, ListProductVenteView, TypeEchangeVenteView, PosteView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

router.register('users', UserAPIView, basename='users')
router.register('typeEchange', TypeEchangeView, basename='type_echange')
router.register('wallet', WalletView, basename='wallet')
router.register('tauxEchange', TauxEchangeView, basename='taux_echange')
router.register('transactions', TransactionsView, basename='transactions')
router.register('basketAgent', BasketForAgentView, basename='basketAgent')
router.register('listProductBasket', BasketListView, basename='list_product_basket')
router.register('customers', CustomerView, basename='customers')
router.register('ventes', VenteView, basename='ventes')
router.register('list_product_vente', ListProductVenteView, basename='list_product_vente')
router.register('list_pay_vente', TypeEchangeVenteView, basename='list_pay_vente')
router.register('poste', PosteView, basename='poste')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
