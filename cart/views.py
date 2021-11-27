from django.shortcuts import render, redirect
from .models import Cart
from index.models import TwoPieceSuit

# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(cart_obj.two_piece_suits.all())
    two_piece_suits = cart_obj.two_piece_suits.all()
    total = 0

    for item in two_piece_suits:
        print(item)
        print(item.price)
        total = total + item.price

    cart_obj.total = total
    cart_obj.save()

    return render(request, "cart/cart.html", {})

def cart_update(request):
    obj = TwoPieceSuit.objects.all()[0]
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    
    if obj in cart_obj.two_piece_suits.all():
        cart_obj.two_piece_suits.remove(obj)
    else:
        cart_obj.two_piece_suits.add(obj)

    return  redirect("/")