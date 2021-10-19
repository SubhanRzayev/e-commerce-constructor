from django.contrib import admin
from order.models import *

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)





# from order.models import (
#     Cart,
#     OrderPlaced,
#     Customer,
#     Country,
# )
# # Register your models here.

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['id','product']

# admin.site.register(Country)


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id','user','phone','address','city','state','zipcode']

# @admin.register(OrderPlaced)
# class OrderPlacedAdmin(admin.ModelAdmin):
#     list_display = ['id','user','customer','product','quantity','ordered_date','status']


