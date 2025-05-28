from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from authentification.models import User
from gestion.models import TypeEchange, Wallet, TauxEchange, Transaction, BasketListProducts, BasketAgent, Customer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import userSerializer, TauxEchangeSerializer, WalletSerializer, TypeEchangeSerializer, TransactionSerializer, BasketForAgentSerializer, BasketListProductSerializer, CustomerSerializer

class UserAPIView(ModelViewSet):
    serializer_class = userSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class TauxEchangeView(ModelViewSet):
    serializer_class = TauxEchangeSerializer
    
    def get_queryset(self):
        return TauxEchange.objects.all()
    

class WalletView(ModelViewSet):
    serializer_class = WalletSerializer
    
    def get_queryset(self):
        return Wallet.objects.all()
    
    
class TypeEchangeView(ModelViewSet):
    serializer_class = TypeEchangeSerializer
    
    def get_queryset(self):
        return TypeEchange.objects.all()
    
    
class TransactionsView(ModelViewSet):
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.all()
    
class BasketListView(ModelViewSet):
    serializer_class = BasketListProductSerializer
    
    def get_queryset(self):
        return BasketListProducts.objects.all()
    
class BasketForAgentView(ModelViewSet):
    serializer_class = BasketForAgentSerializer
    
    def get_queryset(self):
        return BasketAgent.objects.filter(is_active = True)
    
class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.all()