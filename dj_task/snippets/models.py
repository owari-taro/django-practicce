from django.db import models
from django.conf import settings
# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

#class Product(Base):
#    label=models.CharField(max_length=200,unique=True)
#    product_id=models.CharField(max_length=250,unique=True)


class Task(Base):
    #id=models.UUIDField(primary_key=True)
    status=models.CharField(max_length=30,default="wating")
    expired_at=models.DateTimeField(null=True,default=None,blank=True)
    old_product=models.FilePathField(default="")
    new_product=models.FilePathField(default="")#.ForeignKey(Product,on_delete=models.CASCADE,related_name="tasks_new")



class Snippet(Base):
    title = models.CharField("title", max_length=128)
    code = models.TextField("code", blank=True)
    description = models.TextField("description", blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class FeedBack(Base):
    product_path=models.FilePathField()
    feature_path=models.FilePathField()
    



class Pref(Base):
    name=models.CharField(max_length=50)
    label=models.CharField(max_length=50)

    def __str__(self):
        return self.label 

class FiscalYear(models.Model):
    year=models.IntegerField(help_text="年度",unique=True)

    def __str__(self):
        return f"{self.year}年度"
 

class QuarterChoices(models.TextChoices):
    BREAD = '1Q', '第一四半期'
    RICE = '2Q', '第二四半期'
    FISH = '3Q', '第三四半期'
    MEAT = '4Q', '第四四半期'


class AcqPeriod(Base):
    fiscal_year=models.ForeignKey(FiscalYear,on_delete=models.CASCADE)
    quarter=models.CharField(choices=QuarterChoices.choices,max_length=30)

    
    def __str__(self):
        return f"{self.fiscal_year} {self.quarter}"





