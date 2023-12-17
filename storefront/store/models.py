from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

class Order(models.Model):
    Pending_status = 'P'
    Complete_status = 'C'
    Failed_status = 'F'
    status_choice = [
        (Pending_status, 'Pending'),
        (Complete_status, 'Complete'),
        (Failed_status, 'Failed')
    ]
    palced_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=status_choice, default=Pending_status)
    
