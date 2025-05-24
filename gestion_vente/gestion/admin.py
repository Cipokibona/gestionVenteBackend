from django.contrib import admin

from .models import Wallet, TauxEchange, TypeEchange, Product, Distributeur, Client, PointOfSell, AchatProduct, ListProductAchat,  ListWalletAchat, VenteProduct, ListProductVente, ListWalletVente

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
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','is_active','date']

@admin.register(Distributeur)
class DistributeurAdmin(admin.ModelAdmin):
    list_display = ['name','adress','tel','is_active','date']
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['respo','fullName','adress','tel','is_active','date']
    
@admin.register(PointOfSell)
class POSAdmin(admin.ModelAdmin):
    list_display = ['respo','fullName','adress','tel','is_active','date']

@admin.register(AchatProduct)
class AchatProductAdmin(admin.ModelAdmin):
    list_display = ['author','distributeur','depot','montantPaye','is_active','date']
    
@admin.register(ListProductAchat)
class ListProductAchatAdmin(admin.ModelAdmin):
    list_display = ['product','achat','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
@admin.register(ListWalletAchat)
class ListWalletAchatAdmin(admin.ModelAdmin):
    list_display = ['achat','wallet','montant','is_active','date']
    
@admin.register(VenteProduct)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['author','client','depot','montantPaye','is_active','date']
    
@admin.register(ListProductVente)
class ListProductVenteAdmin(admin.ModelAdmin):
    list_display = ['product','vente','quantity','pricePerUnitOfficiel','pricePerUnitReel','is_active','date']
    
@admin.register(ListWalletVente)
class ListProductVenteAdmin(admin.ModelAdmin):
    list_display = ['vente','wallet','montant','is_active','date']