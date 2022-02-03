from .models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Customer

@receiver(post_save, sender=Customer)
def create_cart(sender, instance, created, **kwargs):
  if created:
    Cart.objects.create(User=instance)

@receiver(post_save, sender=Cart)
def cal_cart_var(sender, instance, **kwargs):
  pass