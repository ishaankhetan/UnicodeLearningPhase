from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User)

    email=models.EmailField(null=True)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100)
    total_income=models.IntegerField(default=0)
    total_expense=models.IntegerField(default=0)
    total_savings=models.IntegerField(default=0)


'''@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
class Income(models.Model):
    class Meta:
        verbose_name_plural="Income"

    income_ID=models.BigIntegerField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    date=models.DateField(default=now, editable=True)
    income_source=models.CharField(max_length=100,default='')
    income_amount=models.IntegerField()

class Expense(models.Model):
    class Meta:
        verbose_name_plural="Expense"

    expense_ID=models.BigIntegerField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    date=models.DateField(default=now, editable=True)
    expense_cause=models.CharField(max_length=100,default='')
    expense_amount=models.IntegerField()

class Savings(models.Model):
     class Meta:
        verbose_name_plural="Savings"

     savings_ID=models.BigIntegerField(primary_key=True)
     
     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     
     date=models.DateField(default=now, editable=True)
     total_savings=models.IntegerField()
     savings_use=models.CharField(max_length=100,default='')