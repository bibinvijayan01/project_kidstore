from django.contrib import admin
from .models import Profile, Category, Product, Cart, Order, OrderItem, Tracking


# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Tracking)



