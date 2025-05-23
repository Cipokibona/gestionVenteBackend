from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from authentification.models import User
from gestion.models import TypeEchange, Wallet, TauxEchange


class TauxEchangeSerializer(ModelSerializer):
    
    class Meta:
        model = TauxEchange
        fields = ['id','devise','taux','date_start','date_end','is_active']


class WalletSerializer(ModelSerializer):
    wallet_name = SerializerMethodField()
    
    class Meta:
        model = Wallet
        fields = ['id','user','typeEchange','wallet_name','montant','bordereau','is_active','date']
        
    def get_wallet_name(self, obj):
        queryset = obj.typeEchange
        return queryset.nom 


class TypeEchangeSerializer(ModelSerializer):
    
    class Meta:
        model = TypeEchange
        fields = ['id','nom','description','is_bordereau','is_devise','is_active','date']


class userSerializer(ModelSerializer):
    wallet_user = SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name','tel','email','imgProfil','is_agent_commercial','is_staff','is_admin','is_respo_pos','wallet_user','is_active']
        
    def get_wallet_user(self, obj):
        queryset = obj.wallet_user.filter(is_active=True)
        serializer = WalletSerializer(queryset, many=True, required=False)
        return serializer.data