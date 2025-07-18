from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from authentification.models import User
from gestion.models import TypeEchange,  TauxEchange,BasketListProducts, BasketAgent, Customer, ListProductVente, TypeEchangeVente, Vente, Poste, SalaireUser, ResponsablePos, Distributeur, Products, PointVente, ApprovisionnementPos, Achat, ListProductApprovionnement, ListPayAchat, ListPayApprovisionnementPos, ListProductAchat, RendreProduitPos, ProduitRenduPos, TypeEchangeRenduPos, RecouvrementVente, CaissePos, ToolsUser, Depenses, BordereauCaisse, ProductPointVente, RequestAgent, RequestProduct
# , Wallet, Transaction
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import userSerializer, TauxEchangeSerializer, TypeEchangeSerializer, BasketListProductSerializer, CustomerSerializer, VenteSerializer, ListProductVenteSerializer, TypeEchangeVenteSerializer, PosteSerializer, BasketAgentSerializer, SalarUserSerializer, DistributeurSerializer, ProductSerializer, PointVenteSerializer, ResponsablePosSerializer, AchatSerializer, ApprovisionnementPosSerializer, ListProductApprovisionnementSerializer, TypeEchangeApprovSerializer, TypeEchangeAchatSerializer, ListProductAchatSerializer, RendreProduitPosSerializer, ProduitRenduPosSerializer, TypeEchangeRenduPosSerializer, RecouvrementVenteSerializer, CaisseSerializer, ToolsUserSerializer, DepenseSerializer, BordereauCaisseSerializer, ProductInfoVenteSerializer, ToolsInfoSerializer, UserInfoSerializer, ProductPointVenteSerializer, RequestAgentSerializer, RequestProductSerializer
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
        return Customer.objects.filter(is_active = True).order_by('fullName')
    
class VenteView(ModelViewSet):
    serializer_class = VenteSerializer
    
    def get_queryset(self):
        return Vente.objects.filter(is_active = True).order_by('-date')
    
class ListProductVenteView(ModelViewSet):
    serializer_class = ListProductVenteSerializer
    
    def get_queryset(self):
        return ListProductVente.objects.filter(is_active = True)
    
# type echange vente, achat, approvisionnement
class TypeEchangeApprovView(ModelViewSet):
    serializer_class = TypeEchangeApprovSerializer
    
    def get_queryset(self):
        return ListPayApprovisionnementPos.objects.filter(is_active = True)
    
class TypeEchangeAchatView(ModelViewSet):
    serializer_class = TypeEchangeAchatSerializer
    
    def get_queryset(self):
        return ListPayAchat.objects.filter(is_active = True)
    
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
        return Distributeur.objects.filter(is_active = True).order_by('name')
    
class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Products.objects.filter(is_active = True).order_by('name')
    
    
class PointVenteView(ModelViewSet):
    serializer_class = PointVenteSerializer
    
    def get_queryset(self):
        return PointVente.objects.filter(is_active = True).order_by('fullName')
    
    
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
        return Achat.objects.filter(is_active = True).order_by('-date')
    
class ListProductApprovisionnementView(ModelViewSet):
    serializer_class = ListProductApprovisionnementSerializer
    
    def get_queryset(self):
        return ListProductApprovionnement.objects.filter(is_active = True)
    
class ListProductAchatView(ModelViewSet):
    serializer_class = ListProductAchatSerializer
    
    def get_queryset(self):
        return ListProductAchat.objects.filter(is_active = True)
    
# view pour rendre les produits et type echange aux pos
class RendreProduitPosView(ModelViewSet):
    serializer_class = RendreProduitPosSerializer
    
    def get_queryset(self):
        return RendreProduitPos.objects.filter(is_active = True)
    
class ProduitRenduPosView(ModelViewSet):
    serializer_class = ProduitRenduPosSerializer
    
    def get_queryset(self):
        return ProduitRenduPos.objects.filter(is_active = True)
    
class TypeEchangeRenduPosView(ModelViewSet):
    serializer_class = TypeEchangeRenduPosSerializer
    
    def get_queryset(self):
        return TypeEchangeRenduPos.objects.filter(is_active = True)
    
# pour recouvrement
class RecouvrementVenteView(ModelViewSet):
    serializer_class = RecouvrementVenteSerializer
    
    def get_queryset(self):
        return RecouvrementVente.objects.filter(is_active = True)  

# Caisse pour point de vente
class CaisseView(ModelViewSet):
    serializer_class = CaisseSerializer
    
    def get_queryset(self):
        return CaissePos.objects.filter(is_active = True)
    
class BordereauCaisseView(ModelViewSet):
    serializer_class = BordereauCaisseSerializer
    
    def get_queryset(self):
        return BordereauCaisse.objects.filter(is_active = True)
    
# Tools user
class ToolsUserView(ModelViewSet):
    serializer_class = ToolsUserSerializer
    
    def get_queryset(self):
        return ToolsUser.objects.filter(is_active = True).order_by('name')

# Depenses
class DepensesView(ModelViewSet):
    serializer_class = DepenseSerializer
    
    def get_queryset(self):
        return Depenses.objects.filter(is_active = True).order_by('-date')
    
class DepenseSalaireView(ModelViewSet):
    serializer_class = DepenseSerializer
    
    def get_queryset(self):
        return Depenses.objects.filter(is_salaire = True)
    
class DepenseToolsView(ModelViewSet):
    serializer_class = DepenseSerializer
    
    def get_queryset(self):
        return Depenses.objects.filter(is_tool = True)


# product pos
class ProductPointVenteView(ModelViewSet):
    serializer_class = ProductPointVenteSerializer
    
    def get_queryset(self):
        return ProductPointVente.objects.filter(is_active = True)


# product info achat et vente
class ProductInfoVenteView(ModelViewSet):
    serializer_class = ProductInfoVenteSerializer
    
    def get_queryset(self):
        return Products.objects.filter(is_active = True).order_by('name')
    
# depenses user et tools
class ToolsInfoView(ModelViewSet):
    serializer_class = ToolsInfoSerializer
    
    def get_queryset(self):
        return ToolsUser.objects.filter(is_active = True)
    
class UserInfoView(ModelViewSet):
    serializer_class = UserInfoSerializer
    
    def get_queryset(self):
        return User.objects.filter(is_active = True)
    
# request panier
class RequestAgentView(ModelViewSet):
    serializer_class = RequestAgentSerializer
    
    def get_queryset(self):
        return RequestAgent.objects.filter(is_active = True)
    
class RequestProductView(ModelViewSet):
    serializer_class = RequestProductSerializer
    
    def get_queryset(self):
        return RequestProduct.objects.filter(is_active = True)