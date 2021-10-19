from django.db import models
from django.db.models.deletion import SET_NULL
from account.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

from product.models import *

User = get_user_model()

class Order(models.Model):
    #relation
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # information
    date_ordered = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100,null=True)

    if customer is '0.':
        def __str__(self):
            return str(self.id)
    else:
        def __str__(self):
            return self.customer.username



    #Total price
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    #Total items
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all() 
        total = sum([item.quantity for item in orderitems])
        return total

    #Grand total shopping_cost
    @property
    def get_grand_total(self):
        orderitems = self.orderitem_set.all() 
        total = sum([item.get_grands_total for item in orderitems])
        return total
    
    @property
    def grand_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.grand for item in orderitems])
        return total

    






class OrderItem(models.Model):
    #relation
    product = models.ForeignKey(Product,on_delete=SET_NULL,null=True)
    order = models.ForeignKey('Order',on_delete=SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    shipping_cost = models.IntegerField(default=1,blank=True,null=True)
    date_added = models.DateTimeField(timezone.now)


    @property
    def get_total(self):
        if self.product.discount_price and self.product.sale == 0:
            total = self.product.discount_price * self.quantity 
            return total
        elif self.product.discount_price == 0.00 and self.product.sale:
            # price product.price product.sale  
            price  = self.product.price * (100 - self.product.sale) // 100
            total =  price * self.quantity
            return total
        elif self.product.discount_price == 0.00 and self.product.sale == 0:
            total = self.product.price * self.quantity
            return total
        else:
            total = self.product.price * self.quantity
            return total

    

    @property
    def get_grands_total(self):
        if self.product.discount_price and self.product.sale == 0 and self.shipping_cost != 0:
            total = self.product.discount_price * self.quantity  + self.shipping_cost
            print("ezidansjdnakjda")
            return total
        elif self.product.discount_price == 0.00 and self.product.sale and self.shipping_cost != 0:
            # price product.price product.sale  
            price  = self.product.price * (100 - self.product.sale) // 100
            total =  price * self.quantity + self.shipping_cost
            return total
        elif self.product.discount_price == 0.00 and self.product.sale == 0 and self.shipping_cost != 0:
            total = self.product.price * self.quantity + self.shipping_cost
            return total
        else:
            total = self.product.price * self.quantity
            return total 

    @property
    def grand(self):
        if self.shipping_cost:
            total = self.shipping_cost
            return total
        




class ShippingAddress(models.Model):
    #relation
    customer = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    order = models.ForeignKey('Order',on_delete=SET_NULL,null=True)
    phone = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    state = models.CharField(max_length=200,null=True,blank=True)
    zipcode = models.CharField(max_length=200,null=True,blank=True)
    date_added = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.address
    


    
    

    

    