from django.contrib import admin

from .models import Wallet, TauxEchange, TypeEchange

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
