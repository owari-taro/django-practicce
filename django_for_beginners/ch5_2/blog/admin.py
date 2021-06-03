from django.contrib import admin
from .models import Post
# Register your models here.
#we can manage post from the admin interface
admin.site.register(Post)