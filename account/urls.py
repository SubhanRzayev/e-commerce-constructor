# from django.urls import path
# from . import views
from django.urls import path
from django.urls.resolvers import RegexPattern
from django.urls.conf import re_path
from account.views import *
from account.forms import *
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'

urlpatterns = [
    # path("login-register", views.register, name="login-register"),
    # path("login-register/", views.login, name="login"),
    path("login-register/", RegisterView.as_view(), name="login-register"),
    path("my-account/<int:pk>/", MyAccountDetailView.as_view(), name="my-account"),
    path("update-account/<int:pk>/", UpdateAccountView.as_view(), name="update-account"),

    path('login/',CustomLoginView.as_view(),name = "login"),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('logout/', LogoutView.as_view(), name='logout'),
]




