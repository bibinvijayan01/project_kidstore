from django.db import models
from django.contrib.auth.models import User



# Profile model.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)

    address = models.TextField(blank=True, null=True)


    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    pin_code = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.user.username
    
# category model.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# Product model.  
class Product(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name 

# Cart model.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='CartItem')

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart of {self.user.username}'s cart - {self.product.name}"
    
# Order model.
class Order(models.Model):

    payment_method = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('PayPal', 'PayPal'),
        ('Cash on Delivery', 'Cash on Delivery'),
    ]

    status_choices = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=50, choices=payment_method)

    status = models.CharField(max_length=50, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
# OrderItem model.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"

# Tracking model.
class Tracking(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    status = models.CharField(max_length=50)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking for Order {self.order.id} - {self.status}"

# CartItem model.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"


