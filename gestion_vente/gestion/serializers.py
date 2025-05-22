from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from authentification.models import User

class userSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name','tel','email','imgProfil','is_agent_commercial','is_staff','is_admin','is_respo_pos','is_active']