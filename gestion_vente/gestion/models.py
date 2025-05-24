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
    
    # def __str__(self):
    #     return self.username
    
class TauxEchange(models.Model):
    devise = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='devise_type')
    taux = models.FloatField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.devise
    

class Product(models.Model):
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
    

class Client(models.Model):
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_client')
    fullName = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullName
    
class PointOfSell(models.Model):
    respo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respo_POS')
    fullName = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullName
    
    
class AchatProduct(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_achat')
    distributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE, related_name='distributeur_achat')
    depot = models.ForeignKey(PointOfSell, on_delete=models.CASCADE, related_name='recepteur_achat')
    montantPaye = models.FloatField()
    # reste = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ListProductAchat(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_product_achat')
    achat = models.ForeignKey(AchatProduct, on_delete=models.CASCADE, related_name='list_achat')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    pricePerUnitReel = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ListWalletAchat(models.Model):
    achat = models.ForeignKey(AchatProduct, on_delete=models.CASCADE, related_name='achat_wallet')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='list_wallet_achat')
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
class VenteProduct(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_vente')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_vente')
    depot = models.ForeignKey(PointOfSell, on_delete=models.CASCADE, related_name='pos_vente')
    montantPaye = models.FloatField()
    # reste = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ListProductVente(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_product_vente')
    vente = models.ForeignKey(VenteProduct, on_delete=models.CASCADE, related_name='list_vente')
    quantity = models.IntegerField()
    pricePerUnitOfficiel = models.FloatField()
    pricePerUnitReel = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    
class ListWalletVente(models.Model):
    vente = models.ForeignKey(AchatProduct, on_delete=models.CASCADE, related_name='vente_wallet')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='list_wallet_vente')
    montant = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)