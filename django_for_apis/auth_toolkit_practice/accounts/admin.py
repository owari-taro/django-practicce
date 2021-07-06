from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Element
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age',
                    'is_staff', 'is_alive', 'gender']
    fieldsets = UserAdmin.fieldsets + \
        ((None, {'fields': ('age', 'gender', 'is_alive',)}),)
    add_fieldsets = ((None, {'fields': (
        'username', "password1", 'password2', 'email', 'age', 'gender', 'is_alive',)}),)

    # UserAdmin.fieldsets+gt
   # ('username', 'password')
# myModels = [CustomUser, CustomUserAdmin,Element]  # iterable list
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Element)
