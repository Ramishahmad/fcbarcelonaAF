# Generated by Django 3.2.7 on 2021-12-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0027_auto_20211203_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='draft_color',
            field=models.CharField(default='green', max_length=30),
        ),
        migrations.AddField(
            model_name='posts',
            name='draft_or_published',
            field=models.CharField(default='Published', max_length=30),
        ),
        migrations.AlterField(
            model_name='posts',
            name='draft',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='posts',
            name='priority',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]