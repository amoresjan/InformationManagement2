# Generated by Django 3.1.1 on 2020-10-08 17:00

from django.db import migrations, models
import django.db.models.deletion


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
                ('product_brand', models.CharField(max_length=30)),
                ('color', models.CharField(choices=[('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('G', 'Green'), ('Y', 'Yellow'), ('P', 'Purple'), ('O', 'Orange')], max_length=1)),
                ('product_dimension', models.CharField(max_length=30)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('num_items', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/apps/product/img/profile_pictures')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
