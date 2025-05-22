from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    imgProfil = models.TextField(null=True, blank=True)
    is_agent_commercial = models.BooleanField(default=False)
    is_respo_pos = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

   