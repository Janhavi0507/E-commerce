from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from numpy import product
from .models import Cart
from django.contrib.auth.decorators import login_required
from products.models import Product

# Create your views here.

@login_required(login_url='/login/')
def CartListView(request):
  cart = Cart.objects.filter(User=request.user).get()
  product = cart.Products.all()
  context = {
    'object' : cart,
    'Products' : product,
  }
  return render(request, 'product/cart.html', context)

@login_required(login_url='/login/')
def AddToCart(request):
  cart = Cart.objects.filter(User=request.user).get()
  product = Product.objects.filter(product_id=request.POST.get('product_id')).get()
  print(cart)
  print(product)
  if product not in cart.Products.all():
    cart.Products.add(product)
  else:
    cart.Products.remove(product)
  return HttpResponseRedirect(cart.get_absolute_url())
