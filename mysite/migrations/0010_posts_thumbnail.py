# Generated by Django 3.2.7 on 2022-01-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_rename_replay_user_comments_replays_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]