from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_home, name="cart-home"), # Cart Page
    path('update', views.cart_update, name="cart-update") # Updated Cart Page
]