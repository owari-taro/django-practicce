from django import forms
from accounts.models import CustomUser,Inquiry


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
    class Meta:
        model=CustomUser
        fields = ( "username","email","password","origin_group", "roles")
