from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer

class UserSignupForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'DOB', 'gender']
