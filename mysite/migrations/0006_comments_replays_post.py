# Generated by Django 3.2.7 on 2022-01-08 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20220107_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments_replays',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.posts'),
            preserve_default=False,
        ),
    ]
