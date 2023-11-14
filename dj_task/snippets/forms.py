from django import forms
from django.db import models
from snippets.models import Task,Pref,AcqPeriod
from django.core.validators import FileExtensionValidator

class UploadForm(forms.Form):
    """
    画像アップロードフォーム

    :param _type_ forms: _description_
    """    
    new_file = forms.FileField(label="画像",help_text="新時期画像",  validators=[FileExtensionValidator(['zip'],message="zip形式以外は対応していません。")])
    old_file=forms.FileField(label="旧画像",help_text="旧時期画像",validators=[FileExtensionValidator(['zip'],message="zip形式以外は対応していません。")])
   
class FeedBackForm(forms.Form):
    """
    画像アップロードフォーム

    :param _type_ forms: _description_
    """    
    product_file = forms.FileField(widget=forms.ClearableFileInput,validators=[FileExtensionValidator(['zip'])])
    feature_file=forms.FileField(widget=forms.ClearableFileInput,validators=[FileExtensionValidator(['zip'])])
    

class QuarterChoices(models.TextChoices):
    BREAD = '1Q', '第一四半期'
    RICE = '2Q', '第二四半期'
    FISH = '3Q', '第三四半期'
    MEAT = '4Q', '第四四半期'

'''
class FoodForm(forms.Form):
    food = forms.fields.ChoiceField(
        choices=FoodChoices.choices,
        required=True,
        label='食べ物',
        # widget=forms.widgets.Select,
    )
'''



class SearchForm(forms.Form):
    pref=forms.ModelChoiceField(queryset=Pref.objects.all(),label="都道府県")    
    new_fiscal_year=forms.ModelChoiceField(queryset=AcqPeriod.objects.all(),label="年度")
    old_fiscal_year=forms.ModelChoiceField(queryset=AcqPeriod.objects.all(),label="年度")

  #  new_quarter=forms.ChoiceField(choices=QuraterChoices,label="四半期")
   # new_quarter=forms.ChoiceField(choices=QuraterChoices,label="四半期")

