from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.models import Customer


# Create your views here.

def login_user(request):

    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            user = Customer.objects.create_user(username, email, password)
            profile = Customer.objects.create(user=user)
            user.save()
            profile.save()
            return redirect('login')
        else:
            return redirect('register')
    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')