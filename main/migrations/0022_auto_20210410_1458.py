# Generated by Django 2.2.14 on 2021-04-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210410_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questcard',
            name='person1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='questcard',
            name='person2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='questcard',
            name='person3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
