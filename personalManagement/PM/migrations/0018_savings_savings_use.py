# Generated by Django 2.2.4 on 2019-10-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0017_user_total_savings'),
    ]

    operations = [
        migrations.AddField(
            model_name='savings',
            name='savings_use',
            field=models.CharField(default='', max_length=100),
        ),
    ]