from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from authentification.models import User
from gestion.models import TypeEchange, Wallet, TauxEchange, Transaction, Products, BasketAgent, BasketListProducts, WalletTypeBasket


class TransactionSerializer(ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id','author','walletSource','walletCible','montant','bordereau','is_delivered','is_active','date','date_delivered']
        
    def create(self, validated_data):
        transaction = Transaction(
            author = validated_data['author'],
            walletSource = validated_data['walletSource'],
            walletCible = validated_data['walletCible'],
            montant = validated_data['montant'],
            bordereau = validated_data['bordereau'],
            is_delivered = validated_data['is_delivered'],
            )
        transaction.save()
        return transaction

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
    
class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Products
        fields = ['id','name','is_active']
        
class BasketListProductSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = BasketListProducts
        fields = ['id','basket','product','product_name','quantity','pricePerUnitOfficiel','date_expiration','is_active','date']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    
class WalletTypeBasketSerializer(ModelSerializer):
    type_echange_name = SerializerMethodField()
    
    class Meta:
        model = WalletTypeBasket
        fields = ['id','basket','typeEchange','type_echange_name','montant','is_active','date']
        
    def get_type_echange_name(self, obj):
        queryset = obj.typeEchange
        return queryset.nom

class BasketForAgentSerializer(ModelSerializer):
    list_product = SerializerMethodField()
    depot_name = SerializerMethodField()
    wallet_basket = SerializerMethodField()
    
    class Meta:
        model = BasketAgent
        fields = ['id','agent','depot','depot_name','list_product','wallet_basket','is_active','date']
        
    def get_list_product(self, obj):
        queryset = obj.thisproduct_for_basket.filter(is_active = True)
        serializer = BasketListProductSerializer(queryset, many=True, required=False)
        return serializer.data
    
    def get_depot_name(self, obj):
        queryset = obj.depot
        return queryset.fullName
    
    def get_wallet_basket(self, obj):
        queryset = obj.basket_user
        serializer = WalletTypeBasketSerializer(queryset, many=True, required=False)
        return serializer.data