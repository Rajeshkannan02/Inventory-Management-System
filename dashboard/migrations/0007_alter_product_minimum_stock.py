# Generated by Django 4.2.5 on 2023-09-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_product_minimum_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='minimum_stock',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
