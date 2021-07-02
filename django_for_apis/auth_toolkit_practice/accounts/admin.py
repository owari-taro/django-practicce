from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', 'gender']
    fieldsets = UserAdmin.fieldsets+((None, {'fields': ('age','gender',)}),)
    add_fieldsets = UserAdmin.fieldsets+((None, {'fields': ('age','gender',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
