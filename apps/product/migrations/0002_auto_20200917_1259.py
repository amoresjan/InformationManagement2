# Generated by Django 3.1 on 2020-09-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_Color',
            field=models.CharField(choices=[('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('G', 'Green'), ('Y', 'Yellow'), ('B', 'Blue'), ('P', 'Purple'), ('O', 'Orange'), ('P', 'Pink')], max_length=1),
        ),
    ]
