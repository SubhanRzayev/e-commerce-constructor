from django.db import models
from django.http import request
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.forms import ShippingAddres
from django.contrib import messages 
from order.models import *
from product.models import *

# Create your views here.


# def cart(request):
#     return render(request,'cart.html')    


# def checkout(request):
#     return render(request,'checkout.html')   
    

class CartView(ListView):
    model = Order
    template_name = 'cart.html'
    success_url = 'order:cart'

class CheckoutView(LoginRequiredMixin,CreateView):
    model = Order
    template_name = 'checkout.html'
    success_url = reverse_lazy('order:checkout')
    form_class= ShippingAddres

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user
        order,created = Order.objects.get_or_create(customer = self.request.user,complete=False)
        
        context["items"] = order.orderitem_set.all() 
        context['order'] = Order.objects.get_or_create(customer = self.request.user,complete=False)
        context['get_cart_total'] = order.get_cart_total
        context['get_grand_total'] = order.get_grand_total
        context['grand_total'] = order.grand_total

        return context
    
    def form_valid(self,form):
        form.save()
        messages.info(request,"Muracietiniz qebul olundu")
        return super().form_valid(form)

    

    
