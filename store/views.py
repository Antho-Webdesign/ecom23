from django.shortcuts import render

from store.models import Product


# Create your views here.
def home(request):
    queryset = Product.objects.all()
    context = {
        'products': queryset
    }
    return render(request, 'home.html', context)

