# Generated by Django 2.2.14 on 2021-04-01 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_questboard_questcards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questboard',
            name='questcards',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Questcard'),
        ),
    ]