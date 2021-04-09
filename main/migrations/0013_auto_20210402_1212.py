# Generated by Django 2.2.14 on 2021-04-02 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210402_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questboard',
            name='questcards',
        ),
        migrations.AddField(
            model_name='questcard',
            name='questboard',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Questboard'),
            preserve_default=False,
        ),
    ]
