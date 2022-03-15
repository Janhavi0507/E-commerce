"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path

appname = 'product'

urlpatterns = [
  path('product/', ProductListView.as_view(), name='product_list'),
  path('product/create/', ProductCreateView.as_view(), name='product_create'),
  path('product/<int:pid>/', ProductDetailsView, name='product_details'),
  path('<int:id>/update/', ProductUpdateView.as_view(), name='product_update'),
  path('<int:id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]