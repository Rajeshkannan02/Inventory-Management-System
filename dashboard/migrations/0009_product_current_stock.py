# Generated by Django 4.2.5 on 2023-10-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_product_minimum_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_stock',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
