# Generated by Django 3.2.7 on 2022-01-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0021_remove_conversation_is_seen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='ssen_time',
            new_name='seen_time',
        ),
    ]
