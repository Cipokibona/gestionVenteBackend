from django.db import models
from authentification.models import User


class TypeEchange(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    is_bordereau = models.BooleanField(default=False)
    is_devise = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

# non utiliser
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet_user')
#     typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='wallet_type')
#     montant = models.FloatField()
#     is_active = models.BooleanField(default=True)
#     date = models.DateTimeField(auto_now_add=True)
    
    
class TauxEchange(models.Model):
    devise = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='devise_type')
    taux = models.FloatField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.devise
    
    
class Distributeur(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    distributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE, related_name='distributeur_product')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_customer')
    fullName = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullName
    

    
class PointVente(models.Model):
    # respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_POS')
    fullName = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullName
    
class ResponsablePos(models.Model):
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_POS')
    pos = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='son_POS')
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
 

class BasketAgent(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent_stock')
    depot = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_stock')
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class Vente(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='client_vente')
    panier = models.ForeignKey(BasketAgent, on_delete=models.CASCADE, related_name='panier_vente')
    reste = models.FloatField()
    date_recouvrement = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ApprovisionnementPos(models.Model):
    posDistributeur = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_distributeur')
    posCible = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_recepteur')
    montant = models.FloatField()
    reste = models.FloatField()
    date_recouvrement = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class Achat(models.Model):
    distributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE, related_name='distributeur_achat')
    posCible = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_cible')
    montant = models.FloatField()
    reste = models.FloatField()
    date_recouvrement = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
# en stock dans le point de vente 
class ProductPointVente(models.Model):
    pos = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='product_of_pos')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='in_product_pos')
    quantity = models.IntegerField()
    quantity_max = models.IntegerField()
    prixAchat = models.FloatField()
    prixVente = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
# list product approvisionnement

class ListProductApprovionnement(models.Model):
    approvisionnement = models.ForeignKey(ApprovisionnementPos, on_delete=models.CASCADE, related_name='origin_pos_product')
    # stock = models.ForeignKey(ProductPointVente, on_delete=models.CASCADE, related_name='product_appro_from')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_appro_for')
    quantity = models.IntegerField()
    prixAchat = models.FloatField()
    prixVente = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ListPayApprovisionnementPos(models.Model):
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='approv_money_echange')
    approvisionnement = models.ForeignKey(ApprovisionnementPos, on_delete=models.CASCADE, related_name='type_on_approv')
    montant = models.FloatField()
    bordereau =  models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

class ListProductAchat(models.Model):
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='product_achat_info')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_distr_for')
    quantity = models.IntegerField()
    prixAchat = models.FloatField()
    prixVente = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)


class BasketListProducts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_for_agent')
    basket = models.ForeignKey(BasketAgent, on_delete=models.CASCADE, related_name='thisproduct_for_basket')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

# non utilise
class WalletTypeBasket(models.Model):
    basket = models.ForeignKey(BasketAgent, on_delete=models.CASCADE, related_name='basket_user')
#     typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='type_echange_basket')
#     montant = models.FloatField()
#     bordereau = models.CharField(max_length=100, null=True)
#     is_active = models.BooleanField(default=True)
#     date = models.DateTimeField(auto_now_add=True)
    
    
class ListProductVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='list_vente')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_vente')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    pricePerUnitClient = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

class TypeEchangeVente(models.Model):
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='vente_money_echange')
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='type_on_vente')
    montant = models.FloatField()
    bordereau =  models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
# pour recouvrement
class RecouvrementVente(models.Model):
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_recouvrement')
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='recouvrement_money_echange')
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='recouvrement_vente')
    montant = models.FloatField()
    bordereau =  models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
     

# non utilise
class Transaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_transaction')
#     walletSource = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_source')
#     walletCible = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_cible')
#     montant = models.FloatField()
#     bordereau = models.CharField(max_length=100, null=True)
#     is_delivered = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date = models.DateTimeField(auto_now_add=True)
#     date_delivered = models.DateTimeField(null=True)
    

class Poste(models.Model):
    name = models.CharField(max_length=100)
    salar = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

class SalaireUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salarie')
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name='son_poste')
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
# pour rendre les produits aux points de vente
class RendreProduitPos(models.Model):
    # class rendre tout meme l'argent
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agent_render')
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='vente_rendu', null=True)
    panier = models.ForeignKey(BasketAgent, on_delete=models.CASCADE, related_name='panier_rendu', null=True)
    recouvrement = models.ForeignKey(RecouvrementVente, on_delete=models.CASCADE, related_name='recouvrement_rendu', null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_render',null=True)
    pos = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_receiver')
    is_received = models.BooleanField(default=False)
    date_received = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ProduitRenduPos(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='produit_rendu')
    render = models.ForeignKey(RendreProduitPos, on_delete=models.CASCADE, related_name='render_product_pos')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
   
# pour rendre argent a pos
    
class TypeEchangeRenduPos(models.Model):
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='typeEchange_rendu')
    render = models.ForeignKey(RendreProduitPos, on_delete=models.CASCADE, related_name='render_typeEchange_pos')
    montant = models.FloatField()
    bordereau =  models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
# caisse pour pos
class CaissePos(models.Model):
    pos = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_caisse')
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='type_echange_caisse')
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class BordereauCaisse(models.Model):
    caisse = models.ForeignKey(CaissePos, on_delete=models.CASCADE, related_name='bordereau_in_caisse')
    name = models.CharField(max_length=100)
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
# outils de travail
class ToolsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tool_respo')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
# depenses
class Depenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_depense')
    caisse = models.ForeignKey(CaissePos, on_delete=models.CASCADE, related_name='caisse_depense')
    tool = models.ForeignKey(ToolsUser, on_delete=models.CASCADE, related_name='tool_depense', null=True)
    description = models.CharField(max_length=100)
    user_depense = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_depense', null=True)
    montant = models.FloatField()
    is_salaire = models.BooleanField(default=False)
    is_tool = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
# list achat
class ListPayAchat(models.Model):
    caisse = models.ForeignKey(CaissePos, on_delete=models.CASCADE, related_name='achat_money_echange')
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='type_on_achat')
    montant = models.FloatField()
    bordereau =  models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

# request du panier
class RequestAgent(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_agent')
    pos = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='request_pos')
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class RequestProduct(models.Model):
    request = models.ForeignKey(RequestAgent, on_delete=models.CASCADE, related_name='request')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='request_product')
    quantity = models.IntegerField()
    prixVente = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
