from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.username # f'{self.first_name} {self.last_name}'


class Account(models.Model):
    acc_type = (
        ("Buyer",'Buyer'),
        ("Seller",'Seller'),
        ("Dealer",'Dealer'),
    )
    User = models.ForeignKey(Customer, on_delete=models.CASCADE)
    image = models.ImageField(default = 'no_picture.png')
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15)
    Address = models.TextField(blank=True)
    account_type = models.CharField(max_length=200, choices=acc_type, default='Seller')

    class Meta:
        unique_together = (('User', 'account_type'),)

    def __str__(self):
        return f'{self.User} ({self.account_type})'

# user details will be private except user_id which will be hashed value