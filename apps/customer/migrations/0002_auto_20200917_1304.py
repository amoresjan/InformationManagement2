# Generated by Django 3.1 on 2020-09-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='barangay',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='street',
            field=models.CharField(default='', max_length=50),
        ),
    ]