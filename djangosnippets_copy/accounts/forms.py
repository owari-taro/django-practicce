from django import forms
from accounts.models import CustomUser,Inquiry,CustomGroup


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = 'disabled'
    class Meta:
        model = CustomUser
        fields = ( "username","origin_group", "roles")


class InquiryForm(forms.ModelForm):
    class Meta:
        model=Inquiry
        fields=("username","message","email")

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id')
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['origin_group'].queryset = CustomGroup.objects.filter(group_id=group_id)   
    
    class Meta:
        model=CustomUser
        fields = ( "username","email","password","origin_group", "roles")

class ResetForm(forms.Form):
    password=forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)