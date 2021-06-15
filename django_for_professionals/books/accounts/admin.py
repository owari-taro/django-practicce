from django_for_professionals.books.accounts.forms import CustomUserChangeForm, CustomuserCreationForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()
# Register your models here.


class CustomuserAdmin(UserAdmin):
    add_form = CustomuserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomuserAdmin)
