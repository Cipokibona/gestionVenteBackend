from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from authentification.models import User
from gestion.models import TypeEchange,  TauxEchange,BasketListProducts, BasketAgent, Customer, ListProductVente, TypeEchangeVente, Vente, Poste, SalaireUser, ResponsablePos, Distributeur, Products, PointVente, ApprovisionnementPos, Achat, ListProductApprovionnement
# , Wallet, Transaction
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import userSerializer, TauxEchangeSerializer, TypeEchangeSerializer, BasketListProductSerializer, CustomerSerializer, VenteSerializer, ListProductVenteSerializer, TypeEchangeVenteSerializer, PosteSerializer, BasketAgentSerializer, SalarUserSerializer, DistributeurSerializer, ProductSerializer, PointVenteSerializer, ResponsablePosSerializer, AchatSerializer, ApprovisionnementPosSerializer, ListProductApprovisionnementSerializer
# , TransactionSerializer, BasketForAgentSerializer, WalletSerializer

class UserAPIView(ModelViewSet):
    serializer_class = userSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class TauxEchangeView(ModelViewSet):
    serializer_class = TauxEchangeSerializer
    
    def get_queryset(self):
        return TauxEchange.objects.all()
    

# class WalletView(ModelViewSet):
#     serializer_class = WalletSerializer
    
#     def get_queryset(self):
#         return Wallet.objects.all()
    
    
class TypeEchangeView(ModelViewSet):
    serializer_class = TypeEchangeSerializer
    
    def get_queryset(self):
        return TypeEchange.objects.all()
    
    
# class TransactionsView(ModelViewSet):
#     serializer_class = TransactionSerializer
    
#     def get_queryset(self):
#         return Transaction.objects.all()
    
class BasketListView(ModelViewSet):
    serializer_class = BasketListProductSerializer
    
    def get_queryset(self):
        return BasketListProducts.objects.all()
    
# class BasketForAgentView(ModelViewSet):
#     serializer_class = BasketForAgentSerializer
    
#     def get_queryset(self):
#         return BasketAgent.objects.filter(is_active = True)
    
class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.filter(is_active = True)
    
class VenteView(ModelViewSet):
    serializer_class = VenteSerializer
    
    def get_queryset(self):
        return Vente.objects.filter(is_active = True).order_by('-date')
    
class ListProductVenteView(ModelViewSet):
    serializer_class = ListProductVenteSerializer
    
    def get_queryset(self):
        return ListProductVente.objects.filter(is_active = True)
    
class TypeEchangeVenteView(ModelViewSet):
    serializer_class = TypeEchangeVenteSerializer
    
    def get_queryset(self):
        return TypeEchangeVente.objects.filter(is_active = True)
    

class PosteView(ModelViewSet):
    serializer_class = PosteSerializer
    
    def get_queryset(self):
        return Poste.objects.filter(is_active = True)
    

class BasketAgentView(ModelViewSet):
    serializer_class = BasketAgentSerializer
    
    def get_queryset(self):
        return BasketAgent.objects.filter(is_active = True)
    
    
class SalarUserView(ModelViewSet):
    serializer_class = SalarUserSerializer
    
    def get_queryset(self):
        return SalaireUser.objects.filter(is_active = True)

class DistributeurView(ModelViewSet):
    serializer_class = DistributeurSerializer
    
    def get_queryset(self):
        return Distributeur.objects.filter(is_active = True)
    
class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(is_active = True)
    
    
class PointVenteView(ModelViewSet):
    serializer_class = PointVenteSerializer
    
    def get_queryset(self):
        return PointVente.objects.filter(is_active = True)
    
    
class RespoPosView(ModelViewSet):
    serializer_class = ResponsablePosSerializer
    
    def get_queryset(self):
        return ResponsablePos.objects.filter(is_active = True)
    

class ApprovisionnementPosView(ModelViewSet):
    serializer_class = ApprovisionnementPosSerializer
    
    def get_queryset(self):
        return ApprovisionnementPos.objects.filter(is_active = True)
    

class AchatView(ModelViewSet):
    serializer_class = AchatSerializer
    
    def get_queryset(self):
        return Achat.objects.filter(is_active = True)
    
class ListProductApprovisionnementView(ModelViewSet):
    serializer_class = ListProductApprovisionnementSerializer
    
    def get_queryset(self):
        return ListProductApprovionnement.objects.filter(is_active = True)