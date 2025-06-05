from django.utils import timezone
from rest_framework.exceptions import NotFound
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from authentification.models import User
from gestion.models import TypeEchange, TauxEchange, Products, BasketAgent, BasketListProducts, WalletTypeBasket, Customer, ListProductVente, TypeEchangeVente, Vente, Poste, SalaireUser, ResponsablePos, Distributeur, PointVente, ProductPointVente, ApprovisionnementPos, Achat, ListProductAchat, ListProductApprovionnement, ListPayApprovisionnementPos, ListPayAchat, ProduitRenduPos, RendreProduitPos


# class TransactionSerializer(ModelSerializer):
    
#     class Meta:
#         model = Transaction
#         fields = ['id','author','walletSource','walletCible','montant','bordereau','is_delivered','is_active','date','date_delivered']
        
#     def create(self, validated_data):
#         transaction = Transaction(
#             author = validated_data['author'],
#             walletSource = validated_data['walletSource'],
#             walletCible = validated_data['walletCible'],
#             montant = validated_data['montant'],
#             bordereau = validated_data['bordereau'],
#             is_delivered = validated_data['is_delivered'],
#             )
#         transaction.save()
#         return transaction

class TauxEchangeSerializer(ModelSerializer):
    
    class Meta:
        model = TauxEchange
        fields = ['id','devise','taux','date_start','date_end','is_active']
        
    def create(self, validated_data):
        taux = TauxEchange.objects.filter(devise=validated_data['devise'], is_active=True).first()
        
        if taux:
            taux.is_active = False
            taux.date_end = timezone.now()
            taux.save()
        
        new_taux = TauxEchange.objects.create(**validated_data)
        return new_taux
    
class ListProductApprovisionnementSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = ListProductApprovionnement
        fields = ['id','approvisionnement','quantity','prixAchat','prixVente','date_expiration','product','product_name','is_active','date']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    
    def create(self, validated_data):
        approvisionnement = validated_data['approvisionnement']
        productPosDistr = ProductPointVente.objects.get(
            pos = approvisionnement.posDistributeur,
            product = validated_data['product']
        )
        productPosDistr.quantity = productPosDistr.quantity - validated_data['quantity']
        productPosDistr.save()
        productPosCible = ProductPointVente(
            pos=approvisionnement.posCible,
            product = validated_data['product'],
            quantity = validated_data['quantity'],
            prixAchat = validated_data['prixAchat'],
            prixVente = validated_data['prixVente'],
            date_expiration = validated_data['date_expiration']
            )
        productPosCible.save()
        
        newProduct = ListProductApprovionnement(
            approvisionnement = approvisionnement,
            product = validated_data['product'],
            quantity = validated_data['quantity'],
            prixAchat = validated_data['prixAchat'],
            prixVente = validated_data['prixVente'],
            date_expiration = validated_data['date_expiration']
            )
        newProduct.save()
        
        return newProduct
        
class ListProductAchatSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = ListProductAchat
        fields = ['id','achat','product','product_name','quantity','prixAchat','prixVente','date_expiration','is_active','date']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    
    def create(self, validated_data):
        achat = validated_data['achat']
        productPosCible = ProductPointVente(
            pos=achat.posCible,
            product = validated_data['product'],
            quantity = validated_data['quantity'],
            prixAchat = validated_data['prixAchat'],
            prixVente = validated_data['prixVente'],
            date_expiration = validated_data['date_expiration']
            )
        productPosCible.save()
        
        newProduct = ListProductAchat(
            achat = achat,
            product = validated_data['product'],
            quantity = validated_data['quantity'],
            prixAchat = validated_data['prixAchat'],
            prixVente = validated_data['prixVente'],
            date_expiration = validated_data['date_expiration']
            )
        newProduct.save()
        
        return newProduct


class TypeEchangeSerializer(ModelSerializer):
    taux_echange = SerializerMethodField()
    
    class Meta:
        model = TypeEchange
        fields = ['id','nom','description','is_bordereau','is_devise','taux_echange','is_active','date']
        
    def get_taux_echange(self, obj):
        queryset = obj.devise_type.filter(is_active = True)
        serializer = TauxEchangeSerializer(queryset, many=True, required=False)
        return serializer.data
    
    def update(self, instance, validated_data):
        instance.nom = validated_data['nom']
        instance.description = validated_data['description']
        instance.is_bordereau = validated_data['is_bordereau']
        instance.is_devise = validated_data['is_devise']
        instance.save()
        return instance
    
    def create(self, validated_data):
        type_echange = TypeEchange.objects.create(**validated_data)
        
        # users = User.objects.all()
        
        # for user in users:
        #     new_wallet_user = Wallet(
        #         user = user,
        #         typeEchange = type_echange,
        #         montant = 0,
        #     )
        #     new_wallet_user.save()
            
        return type_echange
    
    
class ProductSerializer(ModelSerializer):
    distributeur_name = SerializerMethodField()
    
    class Meta:
        model = Products
        fields = ['id','distributeur','distributeur_name','name','description','is_active']
        
    def get_distributeur_name(self, obj):
        queryset = obj.distributeur
        return queryset.name
    
class DistributeurSerializer(ModelSerializer):
    product_list = SerializerMethodField()
    
    class Meta:
        model = Distributeur
        fields = ['id','name','product_list','adress','tel','is_active','date']
        
    def get_product_list(self, obj):
        queryset = obj.distributeur_product.filter(is_active = True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data

    
class BasketListProductSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = BasketListProducts
        fields = ['id','basket','product','product_name','quantity','pricePerUnitOfficiel','date_expiration','is_active','date']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    

class CustomerSerializer(ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id','respo','fullName','adress','tel','is_active','date']
        
class ListProductVenteSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = ListProductVente
        fields = ['id','vente','product','product_name','quantity','pricePerUnitOfficiel','pricePerUnitClient','is_active','date']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    
# type d'echange de vente, achat et approvisionnement
class TypeEchangeApprovSerializer(ModelSerializer):
    typeEchange_name = SerializerMethodField()
    
    class Meta:
        model = ListPayApprovisionnementPos
        fields = ['id','typeEchange','typeEchange_name','approvisionnement','montant','bordereau','is_active','date']
        
    def get_typeEchange_name(self, obj):
        queryset = obj.typeEchange
        return queryset.nom
    
class TypeEchangeAchatSerializer(ModelSerializer):
    typeEchange_name = SerializerMethodField()
    
    class Meta:
        model = ListPayAchat
        fields = ['id','typeEchange','typeEchange_name','achat','montant','bordereau','is_active','date']
        
    def get_typeEchange_name(self, obj):
        queryset = obj.typeEchange
        return queryset.nom

class TypeEchangeVenteSerializer(ModelSerializer):
    typeEchange_name = SerializerMethodField()
    
    class Meta:
        model = TypeEchangeVente
        fields = ['id','typeEchange','typeEchange_name','vente','montant','bordereau','is_active','date']
        
    def get_typeEchange_name(self, obj):
        queryset = obj.typeEchange
        return queryset.nom

class VenteSerializer(ModelSerializer):
    product_list = SerializerMethodField()
    typeEchange_list = SerializerMethodField()
    client_name = SerializerMethodField()
    agent_name = SerializerMethodField()
    agent_id = SerializerMethodField()
    pos_name = SerializerMethodField()
    
    class Meta:
        model = Vente
        fields = ['id','client','client_name','panier','agent_id','agent_name','pos_name','product_list','typeEchange_list','reste','date_recouvrement','is_active','date']
        
    def get_product_list(self, obj):
        queryset = obj.list_vente.filter(is_active = True)
        serializer = ListProductVenteSerializer(queryset, many=True)
        return serializer.data
        
    def get_typeEchange_list(self, obj):
        queryset = obj.type_on_vente.filter(is_active = True)
        serializer = TypeEchangeVenteSerializer(queryset, many=True)
        return serializer.data
    
    def get_client_name(self, obj):
        queryset = obj.client
        return queryset.fullName
    
    def get_agent_id(self, obj):
        queryset = obj.panier
        return queryset.agent.id
    
    def get_agent_name(self, obj):
        queryset = obj.panier
        return queryset.agent.username
    
    def get_pos_name(self, obj):
        queryset = obj.panier
        return queryset.depot.fullName
        
    
    def create(self, validated_data):
        vente = Vente.objects.create(**validated_data)  
        return vente
        
class BasketAgentSerializer(ModelSerializer):
    list_product = SerializerMethodField()
    depot_name = SerializerMethodField()
    # basket_vente = SerializerMethodField()
    
    class Meta:
        model = BasketAgent
        fields = ['id','agent','depot','depot_name','list_product','is_active','date']
        
    def get_list_product(self, obj):
        queryset = obj.thisproduct_for_basket.filter(is_active = True)
        serializer = BasketListProductSerializer(queryset, many=True)
        return serializer.data
    
    def get_depot_name(self, obj):
        queryset = obj.depot
        return queryset.fullName
    
    # def get_basket_vente(self, obj):
    #     queryset = obj.panier_vente.filter(is_active = True)
    #     serializer = VenteSerializer(queryset, many=True)
    #     return serializer.data

class SalarUserSerializer(ModelSerializer):
    montant_poste = SerializerMethodField()
    post_name = SerializerMethodField()
    
    class Meta:
        model = SalaireUser
        fields = ['id','user','poste','post_name','montant_poste','is_active','date']
        
    def get_montant_poste(self, obj):
        queryset = obj.poste
        return queryset.salar
    
    def get_post_name(self, obj):
        queryset = obj.poste
        return queryset.name
        
class PosteSerializer(ModelSerializer):
    post_user = SerializerMethodField()
    
    class Meta:
        model = Poste
        fields = ['id','name','post_user','salar','is_active']
        
    def get_post_user(self, obj):
        queryset = obj.son_poste.filter(is_active = True)
        serializer = SalarUserSerializer(queryset, many=True)
        return serializer.data
        
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.salar = validated_data['salar']
        instance.save()
        return instance
    
class ResponsablePosSerializer(ModelSerializer):
    respo_name = SerializerMethodField()
    
    class Meta:
        model = ResponsablePos
        fields = ['id','respo','respo_name','pos','is_active','date']
        
    def get_respo_name(self, obj):
        queryset = obj.respo
        return queryset.username
    
class ProductPointVenteSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    
    class Meta:
        model = ProductPointVente
        fields = ['id','pos','product','product_name','quantity','prixAchat','prixVente','date_expiration','is_active']
        
    def get_product_name(self, obj):
        queryset = obj.product
        return queryset.name
    
class ApprovisionnementPosSerializer(ModelSerializer):
    posDistributeur_name = SerializerMethodField()
    list_product = SerializerMethodField()
    
    class Meta:
        model = ApprovisionnementPos
        fields = ['id','posDistributeur','posDistributeur_name','posCible','montant','reste','list_product','date_recouvrement','is_active','date']
        
    def get_posDistributeur_name(self, obj):
        queryset = obj.posDistributeur
        return queryset.fullName
    
    def get_list_product(self, obj):
        queryset = obj.origin_pos_product.filter(is_active = True)
        serializer = ListProductApprovisionnementSerializer(queryset, many = True)
        return serializer.data
        
class AchatSerializer(ModelSerializer):
    distributeur_name = SerializerMethodField()
    list_product = SerializerMethodField()
    
    class Meta:
        model = Achat
        fields = ['id','distributeur','distributeur_name','posCible','montant','reste','list_product','date_recouvrement','is_active','date']
        
    def get_distributeur_name(self, obj):
        queryset = obj.distributeur
        return queryset.name
    
    def get_list_product(self, obj):
        queryset = obj.product_achat_info.filter(is_active = True)
        serializer = ListProductAchatSerializer(queryset, many = True)
        return serializer.data
    
class PointVenteSerializer(ModelSerializer):
    list_respo = SerializerMethodField()
    list_product = SerializerMethodField()
    
    class Meta:
        model = PointVente
        fields = ['id','fullName','adress','tel','list_respo','list_product','is_active','date']
        
    def get_list_respo(self, obj):
        queryset = obj.son_POS.filter(is_active = True)
        serializer = ResponsablePosSerializer(queryset, many=True)
        return serializer.data
    
    def get_list_product(self, obj):
        queryset = obj.product_of_pos.filter(is_active = True)
        serializer = ProductPointVenteSerializer(queryset, many=True)
        return serializer.data
    
# serializer pour rendre les produits aux pos
class RendreProduitPosSerializer(ModelSerializer):
    
    class Meta:
        model = RendreProduitPos
        fields = ['id','agent','receiver','pos','is_received','date_received','is_active']
        
class ProduitRenduPosSerializer(ModelSerializer):
    
    class Meta:
        model = ProduitRenduPos
        fields = ['id','product','render','quantity','pricePerUnitOfficiel','date_expiration','is_active']
        
    
class userSerializer(ModelSerializer):
    # wallet_user = SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name','tel','email','imgProfil','is_agent_commercial','is_admin','is_respo_pos','is_active']
        
    # def get_wallet_user(self, obj):
    #     queryset = obj.wallet_user.filter(is_active=True)
    #     serializer = WalletSerializer(queryset, many=True, required=False)
    #     return serializer.data
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            tel = validated_data['tel'],
            email = validated_data['email'],
            imgProfil = validated_data['imgProfil'],
            is_agent_commercial = validated_data['is_agent_commercial'],
            is_admin = validated_data['is_admin'],
            is_respo_pos = validated_data['is_respo_pos']
        )
        user.set_password(validated_data['password'])  # Hachage du mot de passe
        user.save()
        
        # type_echanges = TypeEchange.objects.all()
        
        # for type_echange in type_echanges:
        #     new_wallet = Wallet(
        #         user = user,
        #         typeEchange = type_echange,
        #         montant = 0,
        #     )
        #     new_wallet.save()
        
        return user
