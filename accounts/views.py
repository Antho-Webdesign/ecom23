from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Customer, Profile
from store.models import Product


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



def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    products = Product.objects.all()
    context = {
        'products': products,
        'profile': profile,
        'user': user,
    }
    if request.method == "POST":
        # traiter le formulaire
        image = request.FILES.get("image")
        profile.image = image
        profile.save()
        return redirect('profile')

    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    pass
    '''
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile,
    }
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        country = request.POST.get("country")
        user.username = username
        user.email = email
        profile.phone = phone
        profile.address = address
        profile.city = city
        profile.zip_code = zip_code
        profile.state = state
        profile.country = country
        message = "Your profile has been updated successfully"
        msg = {
            'message': message,
        }
        context.update(msg)

        user.save()
        profile.save()
        return redirect('profile')
        '''
    return render(request, 'accounts/profile_update.html')