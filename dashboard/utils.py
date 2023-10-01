

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, StaffRequest

@receiver(post_save, sender=StaffRequest)
def check_low_stock(sender, instance, **kwargs):
    product = instance.product
    if product.quantity - instance.request_quantity < product.minimum_quantity:
        # Implement your notification logic here, e.g., send an email or update a notification flag
        # You can use a notification library or create your custom notification system
        # For simplicity, we'll print a message to the console
        print(f"Low stock alert for product: {product.name}")
