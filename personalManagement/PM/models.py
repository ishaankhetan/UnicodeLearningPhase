from django.db import models
from django.utils.timezone import now

# Create your models here.

class User(models.Model):
    user_ID=models.BigIntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)
    total_income=models.IntegerField(default=0)
    total_expense=models.IntegerField(default=0)
    total_savings=models.IntegerField(default=0)

'''class UserExpense(models.Model):
    class Meta:
        verbose_name_plural="User Expenses"
    user_expense_ID=models.IntegerField(primary_key=True)
    user_ID=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    

class UserIncome(models.Model):
    class Meta:
        verbose_name_plural="User Incomes"
    user_income_ID=models.IntegerField(primary_key=True)
    user_ID=models.OneToOneField(User,on_delete=models.CASCADE,default=1)'''
   

class Expense(models.Model):
    class Meta:
        verbose_name_plural="Expense"
    expense_ID=models.BigIntegerField(primary_key=True)
    user_ID=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date=models.DateField(default=now, editable=True)
    expense_cause=models.CharField(max_length=100,default='')
    #frequency=models.IntegerField()
    expense_amount=models.IntegerField()

class Income(models.Model):
    class Meta:
        verbose_name_plural="Income"
    income_ID=models.BigIntegerField(primary_key=True)
    user_ID=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date=models.DateField(default=now, editable=True)
    income_source=models.CharField(max_length=100,default='')
    income_amount=models.IntegerField()

class Savings(models.Model):
     class Meta:
        verbose_name_plural="Savings"
     savings_ID=models.BigIntegerField(primary_key=True)
     user_ID=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
     date=models.DateField(default=now, editable=True)
     total_savings=models.IntegerField()
     savings_use=models.CharField(max_length=100,default='')
