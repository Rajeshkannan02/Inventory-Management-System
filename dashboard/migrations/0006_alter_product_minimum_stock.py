# Generated by Django 4.2.5 on 2023-09-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_product_minimum_stock_staffrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='minimum_stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]