from django.db import models
from customers.models import Customer
from django.urls import reverse
from products.models import Product

# Create your models here.

class Cart(models.Model):
  User = models.ForeignKey(Customer, on_delete=models.CASCADE)
  Cart_Id = models.AutoField(primary_key=True)
  Cart_name = models.CharField(max_length=200, default='Cart 1')
  Total_Items = models.PositiveIntegerField(default=0)
  Bill_Total = models.PositiveIntegerField(default=0)
  Created_At = models.DateTimeField(auto_now_add=True)
  Products = models.ManyToManyField(Product)

  def __str__(self):
    return f'{self.Cart_name} ({self.User.username})'

  def get_absolute_url(self):
    return reverse("userCart")
  
  def calculateTotalItems(self):
    self.Total_Items = self.Products.count()

  def getCartId(self):
    return self.Cart_Id