from django.contrib import admin

from .models import TauxEchange, TypeEchange, Products, Distributeur, Customer, PointVente, BasketAgent, Vente, ListProductVente, TypeEchangeVente, Poste, BasketListProducts, ResponsablePos, SalaireUser, ProductPointVente, ApprovisionnementPos, Achat,ListProductApprovionnement, ListProductAchat, ListPayAchat, ListPayApprovisionnementPos
# , BuyProduct, AllProductAchat,  AllWalletBuy, SellProduct, AllProductVente, AllWalletVente, Transaction, WalletTypeBasket

@admin.register(TypeEchange)
class CustomTypeEchangeAdmin(admin.ModelAdmin):
    list_display = ['nom','description','is_bordereau','is_devise','is_active','date']
    search_fields = ('nom','is_bordereau','is_devise','is_active',)
    list_filter = ('nom','is_bordereau','is_devise','is_active',)
    
# @admin.register(Wallet)
# class CustomWalletAdmin(admin.ModelAdmin):
#     list_display = ['user','typeEchange','montant','is_active','date']
#     search_fields = ('user','typeEchange',)
    
@admin.register(TauxEchange)
class TauxEchangeAdmin(admin.ModelAdmin):
    list_display = ['devise','taux','date_start','date_end','is_active']
    
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['distributeur','name','description','is_active','date']

@admin.register(Distributeur)
class DistributeurAdmin(admin.ModelAdmin):
    list_display = ['name','adress','tel','is_active','date']
    
@admin.register(Customer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['respo','fullName','adress','tel','is_active','date']
    
@admin.register(PointVente)
class POSAdmin(admin.ModelAdmin):
    list_display = ['fullName','adress','tel','is_active','date']
    
@admin.register(ResponsablePos)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ['respo','pos','is_active','date']

@admin.register(SalaireUser)
class SalaireAdmin(admin.ModelAdmin):
    list_display = ['user','poste','is_active','date']

# @admin.register(BuyProduct)
# class AchatProductAdmin(admin.ModelAdmin):
#     list_display = ['author','distributeur','depot','montantPaye','is_active','date']
    
# @admin.register(AllProductAchat)
# class ListProductAchatAdmin(admin.ModelAdmin):
#     list_display = ['product','achat','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
# @admin.register(AllWalletBuy)
# class ListWalletAchatAdmin(admin.ModelAdmin):
#     list_display = ['buy','wallet','montant','is_active','date']
    
# @admin.register(SellProduct)
# class VenteAdmin(admin.ModelAdmin):
#     list_display = ['author','client','depot','montantPaye','is_active','date']
    
# @admin.register(AllProductVente)
# class ListProductVenteAdmin(admin.ModelAdmin):
#     list_display = ['product','vente','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
# @admin.register(AllWalletVente)
# class ListProductVenteAdmin(admin.ModelAdmin):
#     list_display = ['vente','wallet','montant','is_active','date']
    
@admin.register(ListProductApprovionnement)
class ListProductApprovionnementAdmin(admin.ModelAdmin):
    list_display = ['approvisionnement','product','quantity','prixAchat','prixVente','date_expiration','is_active','date']
    
@admin.register(ListProductAchat)
class ListProductAchatAdmin(admin.ModelAdmin):
    list_display = ['achat','product','quantity','prixAchat','prixVente','date_expiration','is_active','date']
    
@admin.register(BasketAgent)
class BasketAgentAdmin(admin.ModelAdmin):
    list_display = ['agent','depot','is_active','date']
    
@admin.register(BasketListProducts)
class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['product','basket','quantity','pricePerUnitOfficiel','date_expiration','is_active','date']
    
# @admin.register(WalletTypeBasket)
# class WalletUserPosAdmin(admin.ModelAdmin):
#     list_display = ['basket','typeEchange','montant','is_active','date']
    
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['client','panier','reste','date_recouvrement','is_active','date']
    
@admin.register(ListProductVente)
class ListProductVenteAdmin(admin.ModelAdmin):
    list_display = ['vente','product','quantity','pricePerUnitOfficiel','pricePerUnitClient','is_active','date']
    
@admin.register(TypeEchangeVente)
class TypeEchangeVenteAdmin(admin.ModelAdmin):
    list_display = ['typeEchange','vente','montant','bordereau','is_active','date']
    
@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ['name','salar','is_active']
    
@admin.register(ProductPointVente)
class ProductPointVenteAdmin(admin.ModelAdmin):
    list_display = ['pos','product','quantity','prixAchat','prixVente','date_expiration','is_active']
    
@admin.register(ApprovisionnementPos)
class ApprovisionnementPosAdmin(admin.ModelAdmin):
    list_display = ['posDistributeur','posCible','montant','reste','date_recouvrement','is_active','date']
    
@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ['distributeur','posCible','montant','reste','date_recouvrement','is_active','date']
    
# liste de pay achat et approvisionnement

@admin.register(ListPayApprovisionnementPos)
class ListPayApprovisionnementPosAdmin(admin.ModelAdmin):
    list_display = ['typeEchange','approvisionnement','montant','bordereau','is_active','date']
    
@admin.register(ListPayAchat)
class ListPayAchatAdmin(admin.ModelAdmin):
    list_display = ['typeEchange','achat','montant','bordereau','is_active','date']