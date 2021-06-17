from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()
# Register your models here.


class CustomuserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]  # git a


admin.site.register(CustomUser, CustomuserAdmin)
