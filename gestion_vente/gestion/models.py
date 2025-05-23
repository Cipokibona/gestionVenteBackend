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
    
    def __str__(self):
        return self.user
    
class TauxEchange(models.Model):
    devise = models.ForeignKey(TypeEchange, on_delete=models.CASCADE, related_name='devise_type')
    taux = models.FloatField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    
    def __str__(self):
        return self.devise