# Generated by Django 4.2.5 on 2023-09-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product',
        ),
    ]
