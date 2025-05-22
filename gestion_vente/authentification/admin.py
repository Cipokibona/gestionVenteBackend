from django.contrib import admin

from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'imgProfil', 'email', 'first_name', 'last_name', 'is_staff', 'is_agent_commercial', 'is_respo_pos', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)