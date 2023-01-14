from django.shortcuts import render

from store.models import Product

# navabar
def navbar(request):
    queryset = Product.objects.all()
    context = {
        'products': queryset
    }
    return render(request, 'include/navbar.html', context)


# home
def home(request):
    return render(request, 'home.html')

