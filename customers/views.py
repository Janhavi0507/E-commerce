from django.shortcuts import render, redirect
from .models import Account, Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def BaseView(request):
  return render(request, 'html/base.html', {})

def HomeView(request):
  
  return render(request, 'html/home.html', {})

def Signup(request):
  if request.method == 'POST':
    username = request.POST['uname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    # confirm password
    if len(username) > 12 or len(username) < 5:
      messages.error(request, 'Username should have length between 5 to 12 characters')
      return redirect('signup')
    if not username.isalnum():
      messages.error(request, 'Username should not contain special characters')
      return redirect('signup')
    if len(pass1) > 16 or len(pass1) < 8:
      messages.error(request, 'Password should have length between 8 to 16 characters')
      return redirect('signup')
    if pass1 != pass2:
      messages.error(request, 'Passwords do not match')
      return redirect('signup')

    # create user
    user = Customer.objects.create_user(username=username, password=pass1)
    user.first_name = fname
    user.last_name = lname
    user.email = email
    user.save()
    account = Account.objects.get_or_create(User=user, phone_number=phone)
    messages.success(request, 'Your account was successfully created!')
    return redirect('login')
  return render(request, 'html/signup.html')

def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      messages.info(request, f"You are now logged in as {username}")
      return redirect(f'/Profile/{user.get_username()}/')
    else:
      messages.error(request, "Invalid username or password.")
      return redirect('login')
  return render(request, 'html/login.html')

def Logout(request):
  logout(request)
  messages.success(request, "Successfully Logged Out")
  return redirect('login')

@login_required(login_url='login/')
def ProfilePage(request, username):
  try:
    user = Customer.objects.get(username = username)
  except Customer.DoesNotExist:
    user = None
  context = {
      'user' : user,
  }
  return render(request, 'html/ProfilePage.html', context)