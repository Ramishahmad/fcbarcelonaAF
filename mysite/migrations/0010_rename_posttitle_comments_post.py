# Generated by Django 3.2.7 on 2021-11-23 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_rename_post_comments_posttitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='posttitle',
            new_name='post',
        ),
    ]