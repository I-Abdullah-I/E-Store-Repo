# Generated by Django 3.2.9 on 2021-12-10 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='nationality_range',
        ),
    ]
