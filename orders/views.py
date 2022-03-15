from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Order
from carts.models import Cart

# Create your views here.

def placeorder(request):
  cart = Cart.objects.filter(User=request.user)
  order = Order.objects.create(User_id=request.user)
  return HttpResponseRedirect('Order Placed')