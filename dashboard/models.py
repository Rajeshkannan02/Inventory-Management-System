from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY=(
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food')
)


class Product(models.Model):
    name=models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=200,  choices=CATEGORY, null=True)
    quantity=models.PositiveBigIntegerField(null=True)
    minimum_stock = models.PositiveIntegerField(default=2)
    minimum_quantity = models.PositiveIntegerField(default=2)
    current_stock = models.PositiveIntegerField(default=0)
    description = models.TextField("Default description")
    

    class Meta:
        verbose_name_plural='Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.unique_id

    

class StaffRequest(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    request_quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.staff.username} - {self.product.name} - {self.request_quantity}'


    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} orderd by {self.staff.username}'
    

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=20)
    