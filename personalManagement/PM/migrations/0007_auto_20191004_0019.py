# Generated by Django 2.2.4 on 2019-10-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0006_auto_20191004_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='income',
            name='income_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_ID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userexpense',
            name='user_expense_ID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userincome',
            name='user_income_ID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
