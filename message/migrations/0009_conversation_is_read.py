# Generated by Django 3.2.7 on 2021-12-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_auto_20211230_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
