from django import forms
from PM.models import User
from . import models
#code from here
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["user_ID","first_name","last_name","password","confirm_password","phone","email","address"]
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("passwords does not match")
class LoginForm(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=30)
    login_password = forms.CharField(label='password', widget=forms.PasswordInput)