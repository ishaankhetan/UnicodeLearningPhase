# Generated by Django 2.2.4 on 2019-10-03 20:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0015_savings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userincome',
            name='user_ID',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user_expense_ID',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user_income_ID',
        ),
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='expense',
            name='user_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PM.User'),
        ),
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='income',
            name='user_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PM.User'),
        ),
        migrations.AddField(
            model_name='savings',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='total_expense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='total_income',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserExpense',
        ),
        migrations.DeleteModel(
            name='UserIncome',
        ),
    ]
