# Generated by Django 3.2.9 on 2021-12-09 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='store_id',
        ),
    ]
