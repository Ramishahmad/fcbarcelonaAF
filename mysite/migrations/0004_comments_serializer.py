# Generated by Django 3.2.7 on 2022-01-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_comments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='serializer',
            field=models.BooleanField(default=True),
        ),
    ]
