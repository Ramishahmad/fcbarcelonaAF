# Generated by Django 3.2.7 on 2022-01-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0011_conversation_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
