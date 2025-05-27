from django.contrib import admin

from .models import Wallet, TauxEchange, TypeEchange, Products, Distributeur, Customer, PointVente, BuyProduct, AllProductAchat,  AllWalletBuy, SellProduct, AllProductVente, AllWalletVente, Transaction, BasketAgent, BasketListProducts, WalletTypeBasket

@admin.register(TypeEchange)
class CustomTypeEchangeAdmin(admin.ModelAdmin):
    list_display = ['nom','description','is_bordereau','is_devise','is_active','date']
    search_fields = ('nom','is_bordereau','is_devise','is_active',)
    list_filter = ('nom','is_bordereau','is_devise','is_active',)
    
@admin.register(Wallet)
class CustomWalletAdmin(admin.ModelAdmin):
    list_display = ['user','typeEchange','montant','bordereau','is_active','date']
    search_fields = ('user','typeEchange',)
    
@admin.register(TauxEchange)
class TauxEchangeAdmin(admin.ModelAdmin):
    list_display = ['devise','taux','date_start','date_end','is_active']
    
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','is_active','date']

@admin.register(Distributeur)
class DistributeurAdmin(admin.ModelAdmin):
    list_display = ['name','adress','tel','is_active','date']
    
@admin.register(Customer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['respo','fullName','adress','tel','is_active','date']
    
@admin.register(PointVente)
class POSAdmin(admin.ModelAdmin):
    list_display = ['respo','fullName','adress','tel','is_active','date']

@admin.register(BuyProduct)
class AchatProductAdmin(admin.ModelAdmin):
    list_display = ['author','distributeur','depot','montantPaye','is_active','date']
    
@admin.register(AllProductAchat)
class ListProductAchatAdmin(admin.ModelAdmin):
    list_display = ['product','achat','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
@admin.register(AllWalletBuy)
class ListWalletAchatAdmin(admin.ModelAdmin):
    list_display = ['buy','wallet','montant','is_active','date']
    
@admin.register(SellProduct)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['author','client','depot','montantPaye','is_active','date']
    
@admin.register(AllProductVente)
class ListProductVenteAdmin(admin.ModelAdmin):
    list_display = ['product','vente','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
@admin.register(AllWalletVente)
class ListProductVenteAdmin(admin.ModelAdmin):
    list_display = ['vente','wallet','montant','is_active','date']
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['author','walletSource','walletCible','montant','bordereau','is_delivered','is_active','date','date_delivered']
    
@admin.register(BasketAgent)
class BasketAgentAdmin(admin.ModelAdmin):
    list_display = ['agent','depot','is_active','date']
    
@admin.register(BasketListProducts)
class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['product','basket','quantity','pricePerUnitOfficiel','date_expiration','is_active','date']
    
@admin.register(WalletTypeBasket)
class WalletUserPosAdmin(admin.ModelAdmin):
    list_display = ['basket','typeEchange','montant','is_active','date']