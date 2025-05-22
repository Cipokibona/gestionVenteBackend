from django.shortcuts import render
from authentification.models import User
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import userSerializer

class UserAPIView(ModelViewSet):
    serializer_class = userSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
