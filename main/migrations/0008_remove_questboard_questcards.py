# Generated by Django 2.2.14 on 2021-04-01 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210402_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questboard',
            name='questcards',
        ),
    ]