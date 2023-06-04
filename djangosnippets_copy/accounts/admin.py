from django.contrib import admin
from accounts.models import CustomGroup,CustomUser,Role
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CustomGroup)
admin.site.register(Role)