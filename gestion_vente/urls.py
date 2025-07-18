"""
URL configuration for gestion_vente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from authentification.views import FrontendAppView
from gestion.views import UserAPIView, TypeEchangeView, TauxEchangeView, BasketListView, CustomerView, VenteView, ListProductVenteView, TypeEchangeVenteView, PosteView, BasketAgentView, SalarUserView, DistributeurView, ProductView, PointVenteView, RespoPosView, ApprovisionnementPosView, AchatView, ListProductApprovisionnementView, TypeEchangeApprovView, TypeEchangeAchatView, ListProductAchatView, RendreProduitPosView, ProduitRenduPosView, TypeEchangeRenduPosView, RecouvrementVenteView, CaisseView, ToolsUserView, DepensesView, DepenseSalaireView, DepenseToolsView, BordereauCaisseView, ProductInfoVenteView, ToolsInfoView, UserInfoView, ProductPointVenteView, RequestAgentView, RequestProductView
# , WalletView, TransactionsView, BasketForAgentView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import os
from django.conf import settings
from django.conf.urls.static import static


router = routers.SimpleRouter()

router.register('users', UserAPIView, basename='users')
router.register('typeEchange', TypeEchangeView, basename='type_echange')
router.register('pointVente', PointVenteView, basename='point_vente')
router.register('tauxEchange', TauxEchangeView, basename='taux_echange')
router.register('respoPos', RespoPosView, basename='responsable_pos')
router.register('basketAgent', BasketAgentView, basename='basketAgent')
router.register('listProductBasket', BasketListView, basename='list_product_basket')
router.register('customers', CustomerView, basename='customers')
router.register('ventes', VenteView, basename='ventes')

# list product vente, achat, approvisionnement
router.register('list_product_vente', ListProductVenteView, basename='list_product_vente')
router.register('list_approvisionnement_pos', ListProductApprovisionnementView, basename='list_approvisionnement_pos')
router.register('list_product_achat_pos', ListProductAchatView, basename='list_product_achat_pos')

# list pay vente, achat, approvisionnement
router.register('list_pay_vente', TypeEchangeVenteView, basename='list_pay_vente')
router.register('list_pay_approv_pos', TypeEchangeApprovView, basename='list_pay_approv_pos')
router.register('list_pay_achat_pos', TypeEchangeAchatView, basename='list_pay_achat_pos')

router.register('poste', PosteView, basename='poste')
router.register('salaire', SalarUserView, basename='salaire')
router.register('distributeur', DistributeurView, basename='distributeur')
router.register('product', ProductView, basename='product')
router.register('approvisionnementPos', ApprovisionnementPosView, basename='approvisionnementPos')
router.register('achat', AchatView, basename='achat')

# rendre les produits et type echang
router.register('rendre_produit_pos', RendreProduitPosView, basename='rendre_produit_pos')
router.register('produit_rendu_pos', ProduitRenduPosView, basename='produit_rendu_pos')
router.register('rendre_typeEchange_pos', TypeEchangeRenduPosView, basename='rendre_typeEchange_pos')

# recouvrement
router.register('recouvrement', RecouvrementVenteView, basename='recouvrement')

# caisse de point de vente
router.register('caisse', CaisseView, basename='caisse')
router.register('bordereau_caisse', BordereauCaisseView, basename='bordereau_caisse')

#tools user
router.register('tools', ToolsUserView, basename='tools')

# depenses
router.register('depenses', DepensesView, basename='depenses')
router.register('depense_salaire', DepenseSalaireView, basename='depense_salaire')
router.register('depense_tools', DepenseToolsView, basename='depense_tools')

# info product vente et achat
router.register('info_product_vente_achat', ProductInfoVenteView, basename='info_product_vente_achat')
router.register('product_point_de_vente', ProductPointVenteView, basename='product_point_de_vente')

# info sur depense user et tools
router.register('info_depense_user', UserInfoView, basename='info_depense_user')
router.register('info_depense_tool', ToolsInfoView, basename='info_depense_tool')

# request panier
router.register('request', RequestAgentView, basename='request')
router.register('request_product', RequestProductView, basename='request_product')

urlpatterns = [
    path('', FrontendAppView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    re_path(r'^(?!admin|api|static|assets).*$' , FrontendAppView.as_view(), name='frontend'),
]

urlpatterns += static("/assets/", document_root=os.path.join(settings.BASE_DIR, "static/assets/"))
