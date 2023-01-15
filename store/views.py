from django.shortcuts import render, get_object_or_404

from store.models import Product

# navabar
def navbar(request):
    product = Product.objects.all()
    if name := request.GET.get('search'):
        if request.method == 'GET':
            products = Product.objects.filter(name__icontains=name)
            context = {
                'products': products,
            }
            return render(request, 'include/navbar.html', context)
    context = {
        'products': product,
    }
    return render(request, 'include/navbar.html', context)



# home
def home(request):
    product = Product.objects.all()
    context = {
        'products': product,
    }
    return render(request, 'home.html', context)


# product_detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    price_ttc = product.price * 1.2
    context = {
        'product': product,
        'price_ttc': price_ttc,
    }
    return render(request, 'store/details.html', context)