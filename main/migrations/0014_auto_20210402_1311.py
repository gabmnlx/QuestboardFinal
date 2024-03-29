# Generated by Django 2.2.14 on 2021-04-02 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210402_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questcard',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='questcard',
            old_name='quest',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='questcard',
            name='questboard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Questboard'),
        ),
    ]
