# Generated by Django 4.2.5 on 2023-09-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_product_minimum_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
