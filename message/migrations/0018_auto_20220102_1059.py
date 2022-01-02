# Generated by Django 3.2.7 on 2022-01-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0017_remove_conversation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='unread',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
