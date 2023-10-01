# Generated by Django 4.2.5 on 2023-09-30 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_alter_order_options_rename_name_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='minimum_stock',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='StaffRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
