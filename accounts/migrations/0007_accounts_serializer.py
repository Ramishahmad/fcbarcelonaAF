# Generated by Django 3.2.7 on 2022-01-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211226_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='serializer',
            field=models.BooleanField(default=True),
        ),
    ]
