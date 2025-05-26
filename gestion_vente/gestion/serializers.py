from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from authentification.models import User
from gestion.models import TypeEchange, Wallet, TauxEchange, Transaction


class TransactionSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id','author','walletSource','walletCible','montant','bordereau','is_delivered','is_active','date','date_delivered']

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
    
    def create(self, validated_data):
        typeEchange = TypeEchange.objects.get(nom = validated_data['typeEchange'])
        # sourceWallet = Wallet.objects.get(id = validated_data['walletSource'])
        
        if (typeEchange.is_bordereau):
            newWallet = Wallet(
                user = validated_data['user'],
                typeEchange = validated_data['typeEchange'],
                montant = validated_data['montant'],
                bordereau = validated_data['bordereau']
                )
            newWallet.save()
            # sourceWallet.montant = sourceWallet.montant - validated_data['montant']
            # sourceWallet.save()
            
            return newWallet
        else:
            wallet = Wallet.objects.get(typeEchange = typeEchange)
            wallet.montant = wallet.montant + validated_data['montant']
            wallet.save()
            
            return wallet
        
    def update(self, instance, validated_data):
        if(instance.montant > validated_data['montant']):
            instance.montant = instance.montant - validated_data['montant']
            instance.save()
        return instance

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