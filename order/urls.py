from django.urls import path
from order.views import CartView, CheckoutView

from order import views  
app_name = 'order'

urlpatterns = [
    path("cart/", CartView.as_view(),name='cart'),
    # path("checkout/", views.checkout, name="chekcout")
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    # path("wishlist/", WishlistView.as_view(), name="wishlist"),
]
