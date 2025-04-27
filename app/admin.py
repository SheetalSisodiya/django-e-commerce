from django.contrib import admin
from .models import (
    Customer,
    Product,
    Carts,
    OrderPlaces
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','locality', 'city', 'zipcode', 'state')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'selling_price','discounted_price','description','category','brand','image')

@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ('user','product', 'quantity')

@admin.register(OrderPlaces)
class OrderPlacesAdmin(admin.ModelAdmin):
    list_display = ('customer','product','carts','quantity','ordered_date','status')

