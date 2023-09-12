from django.contrib import admin
from accounts.models import CustomGroup,Role
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group


class CustomGroupAdmin(admin.ModelAdmin):
     def get_queryset(self,request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        group_id=request.user.origin_group.group_id
        return qs.filter(group_id=group_id)


#

class CustomUserAdmin(UserAdmin):
    filedssets={}
    def get_queryset(self,request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        group_id=request.user.origin_group.group_id
        return qs.filter(origin_group__group_id=group_id)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        #https://stackoverflow.com/questions/41880634/django-admin-limit-the-choices-in-dropdown

        if db_field.name == "origin_group":
                kwargs["queryset"] =CustomGroup.objects.filter(group_id=request.user.origin_group.group_id)
        return super(CustomUserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


CustomUser = get_user_model()
# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(CustomGroup,CustomGroupAdmin)
admin.site.register(Role)
