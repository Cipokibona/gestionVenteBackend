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

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet_user')
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='wallet_type')
    montant = models.FloatField()
    bordereau = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
class TauxEchange(models.Model):
    devise = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='devise_type')
    taux = models.FloatField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.devise
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Distributeur(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
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
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_POS')
    fullName = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullName
    
class BuyProduct(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_buy')
    distributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE, related_name='distributeur_bu')
    depot = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='recepteur_buy')
    montantPaye = models.FloatField()
    # reste = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    
class AllProductAchat(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='all_product_achat')
    achat = models.ForeignKey(BuyProduct, on_delete=models.CASCADE, related_name='all_achat')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    pricePerUnitReel = models.FloatField()
    date_expiration = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
class AllWalletBuy(models.Model):
    buy = models.ForeignKey(BuyProduct, on_delete=models.CASCADE, related_name='buy_wallet')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='all_wallet_buy')
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
class SellProduct(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_sell')
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='client_sell')
    depot = models.ForeignKey(PointVente, on_delete=models.CASCADE, related_name='pos_sell')
    montantPaye = models.FloatField()
    # reste = models.FloatField()
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
    
class WalletTypeBasket(models.Model):
    basket = models.ForeignKey(BasketAgent, on_delete=models.CASCADE, related_name='basket_user')
    typeEchange = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='type_echange_basket')
    montant = models.FloatField()
    bordereau = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
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


class AllProductVente(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='all_product_vente')
    vente = models.ForeignKey(SellProduct, on_delete=models.CASCADE, related_name='all_vente')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    pricePerUnitReel = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
     
    
class Transaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_transaction')
    walletSource = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_source')
    walletCible = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_cible')
    montant = models.FloatField()
    bordereau = models.CharField(max_length=100, null=True)
    is_delivered = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(null=True)
    
class AllWalletVente(models.Model):
    vente = models.ForeignKey(BuyProduct, on_delete=models.CASCADE, related_name='sell_wallet')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='all_wallet_sell')
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    