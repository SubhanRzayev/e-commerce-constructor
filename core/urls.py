from django.urls import path
from .views import ContactView,IndexView, SearchView
app_name = 'core'

urlpatterns = [
    # path("", views.home, name="index"),
    path("product-list/s", SearchView.as_view(), name="search"),
    path("", IndexView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),

]
