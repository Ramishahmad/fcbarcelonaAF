# Generated by Django 3.2.7 on 2022-01-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_accounts_serializer'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
    ]
