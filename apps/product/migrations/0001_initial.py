# Generated by Django 3.1.1 on 2020-10-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.AutoField(primary_key=True, serialize=False)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('product_category', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('profile_picture', models.ImageField(null=True, upload_to='static/apps/product/img/profile_pictures')),
                ('product_brand', models.CharField(max_length=30)),
                ('color', models.CharField(choices=[('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('G', 'Green'), ('Y', 'Yellow'), ('B', 'Blue'), ('P', 'Purple'), ('O', 'Orange'), ('P', 'Pink')], max_length=1)),
                ('product_dimension', models.CharField(max_length=30)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('num_items', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
