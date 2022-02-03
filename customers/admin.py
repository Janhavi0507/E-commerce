from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignupForm
from .models import Account, Customer

# Register your models here.

class CustomerAdmin(UserAdmin):
  model = Customer
  add_form = UserSignupForm

  fieldsets = (
    *UserAdmin.fieldsets, (
      'User extra fields', {
        'fields' : (
          'middle_name',
          'DOB',
          'gender',
        )
      }
    )
  )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account)