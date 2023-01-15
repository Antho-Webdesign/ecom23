from django.contrib import admin

from store.models import Category, Product, Order, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)