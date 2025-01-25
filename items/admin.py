from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Customer, Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
