from django.urls import reverse_lazy
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404
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

class ProductDetailsView(DetailView):
  template_name = 'product/product_details.html'
  queryset = Product.objects.all()

  def get_object(self):
    id_ = self.kwargs.get("id")
    return get_object_or_404(Product, product_id = id_)
  
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

