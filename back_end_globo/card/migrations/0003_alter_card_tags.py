# Generated by Django 3.2.8 on 2021-10-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20211030_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
