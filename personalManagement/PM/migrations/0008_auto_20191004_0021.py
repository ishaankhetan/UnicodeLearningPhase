# Generated by Django 2.2.4 on 2019-10-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0007_auto_20191004_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexpense',
            name='user_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PM.User'),
        ),
        migrations.AlterField(
            model_name='userincome',
            name='user_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PM.User'),
        ),
    ]
