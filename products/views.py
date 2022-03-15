from django.urls import reverse_lazy
from carts.models import Cart
from .forms import ProductForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from django.views.generic import (
    CreateView, DetailView, UpdateView, ListView, DeleteView
)

# Create your views here.

class ProductCreateView(CreateView):
  template_name = 'product/product_create.html'
  form_class = ProductForm
  queryset = Product.objects.all()

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

class ProductListView(ListView):
  template_name = 'product/product_list.html'
  queryset = Product.objects.all()

def ProductDetailsView(request, pid):
  product = Product.objects.filter(product_id=pid).get()
  cart = Cart.objects.filter(User=request.user).get()
  context = {
    'object' : product,
    'cart' : cart,
  }
  return render(request, 'product/product_details.html', context)


class ProductUpdateView(UpdateView):
  template_name = 'product/product_update.html'
  form_class = ProductForm
  queryset = Product.objects.all()

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

class ProductDeleteView(DeleteView):
  template_name = 'product/product_delete.html'
  queryset = ProductForm
  success_url = reverse_lazy('product_list')

