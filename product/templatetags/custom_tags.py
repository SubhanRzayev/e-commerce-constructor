from django.template import Library
from product.models import *
from order.models import *

register = Library()



@register.simple_tag
def price(price,sale):
    return price * (100-sale) // 100



@register.simple_tag
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()

        print(items)
    else:
        items = []
        order = {
            "get_cart_total":0,
            "get_cart_items":0,
            "get_grand_total":0,
            "grand_total":0,
        }


        

    context = {
        "items":items,
        "order":order,
    }
    
    return context
        

