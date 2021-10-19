from product.views import ProductView,ProductDetailView
from django.urls import path

app_name = 'product'

urlpatterns = [
    path("product-list/", ProductView.as_view(), name="product_list"),
    path("product-detail/<int:pk>/",ProductDetailView.as_view(), name="product_detail"),
]
