from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.

class Product(models.Model):
  product_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  image = models.ImageField(default = 'no_image.png')
  MRP = models.PositiveIntegerField(default=0)
  sellPrice = models.PositiveBigIntegerField(default=0)

  def get_absolute_url(self):
    return reverse("product_details", kwargs={'pid' : self.product_id})