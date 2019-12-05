from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Income, Expense
class DataForm(forms.ModelForm):
    
    '''phone = forms.IntegerField()
    address=forms.CharField()
    total_income=forms.IntegerField()
    total_expense=forms.IntegerField()
    total_savings=forms.IntegerField()'''
    
    class Meta:
        model = Profile
        fields = ('user', 'email', 'phone', 'address')

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields = ('user', 'income_ID', 'date', 'income_source', 'income_amount')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields = ('user', 'expense_ID', 'date', 'expense_cause', 'expense_amount')