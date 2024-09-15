from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255) #max_length is a required field
    discount = models.FloatField() #FloatField is a required field


class Collection(models.Model):
    title = models.CharField(max_length=255) #max_length is a required field
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True, related_name='+') #on_delete is a required field

class Product(models.Model):
    title = models.CharField(max_length=255) #max_length is a required field
    description = models.TextField() #TextField is a required field
    price = models.DecimalField(max_digits=6, decimal_places=2) #max_digits and decimal_places are required fields
    inventory = models.IntegerField() #IntegerField is a required field
    last_updated = models.DateTimeField(auto_now=True) #auto_now is a required field 
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) #on_delete is a required field
    promotions = models.ManyToManyField(Promotion) #ManyToManyField is a required field


class Customer(models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBERSHIP_GOLD = 'G'
    MEMEBERSHIP_PLATINUM = 'P'
    MEMEBER_CHOICES = [
        (MEMEBERSHIP_BRONZE, 'Bronze'),
        (MEMEBERSHIP_SILVER, 'Silver'),
        (MEMEBERSHIP_GOLD, 'Gold'),
        (MEMEBERSHIP_PLATINUM, 'Platinum'),
    ]
    first_name = models.CharField(max_length=255) #max_length is a required field
    last_name = models.CharField(max_length=255) #max_length is a required field
    email = models.EmailField(unique=True) #unique is a required field
    phone = models.CharField(max_length=20) #max_length is a required field
    birth_date = models.DateField(null=True) #null is a required field
    memember = models.CharField(max_length=1, choices=MEMEBER_CHOICES, default=MEMEBERSHIP_BRONZE) #max_length and choices are required fields
    Order = models.ForeignKey('Order', on_delete=models.CASCADE,related_name='+') #on_delete is a required field

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True) #auto_now_add is a required field
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING) #max_length and choices are required fields
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT) #on_delete is a required field
    OrderItem = models.ForeignKey('OrderItem', on_delete=models.CASCADE,related_name='+') #on_delete is a required field

class Address(models.Model):
    street = models.CharField(max_length=255) #max_length is a required field
    city = models.CharField(max_length=255) #max_length is a required field
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #on_delete is a required field  
    zip= models.CharField(max_length=10,default='000000') #max_length is a required field

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) #on_delete is a required field
    product = models.ForeignKey(Product, on_delete=models.PROTECT) #on_delete is a required field
    quantity = models.PositiveIntegerField() #PositiveIntegerField is a required field
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #max_digits and decimal_places are required fields

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add is a required field


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #on_delete is a required field
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #on_delete is a required field
    quantity = models.PositiveIntegerField() #PositiveIntegerField is a required field