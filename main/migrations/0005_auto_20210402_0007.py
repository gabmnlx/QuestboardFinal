# Generated by Django 2.2.14 on 2021-04-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210401_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questboard',
            name='questcards',
        ),
        migrations.AddField(
            model_name='questcard',
            name='questboard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Questboard'),
        ),
    ]