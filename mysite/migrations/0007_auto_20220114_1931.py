# Generated by Django 3.2.7 on 2022-01-14 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0006_comments_replays_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments_replays',
            name='name',
        ),
        migrations.AddField(
            model_name='comments_replays',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts'),
            preserve_default=False,
        ),
    ]
