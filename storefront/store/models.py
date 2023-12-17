from django.db import models

# Create your models here.
class Collection(models.Model):
    type = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)

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
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key = True)

# the parent class goes to chiled class to tell the relationship

# the primary key help us to create onto one relationship between addres and customer
# the above code shows the way we create tables in database using python code only without database
# choice field shows options we insert in the database