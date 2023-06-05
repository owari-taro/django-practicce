from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updatedat_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomGroup(Base):
    label = models.CharField(max_length=200)
    group_id = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.group_id


class Role(Base):
    name=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    origin_group = models.ForeignKey(
        CustomGroup, null=True, on_delete=models.CASCADE, related_name="users"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    roles=models.ManyToManyField(Role,null=True,blank=True)
   
    def show_roles(self):
        res=" | ".join([each.name for each in self.roles.all() ])
        return res


class Inquiry(Base):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=500)
