# Generated by Django 3.1.4 on 2020-12-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_auto_20201220_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='result_url',
        ),
    ]