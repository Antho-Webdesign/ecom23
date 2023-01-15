from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from store.models import Product


# navabar
def navbar(request):
    user = request.user
    product = Product.objects.all().order_by('-id')

    if name := request.GET.get('search'):
        if request.method == 'GET':
            products = Product.objects.filter(name__icontains=name)
            print('iciiii')

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': product,
        'page_obj': page_obj,
        'user': user,
    }
    return render(request, 'include/navbar.html', context)


# home
def home(request):
    product = Product.objects.all()
    paginator = Paginator(product, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': product,
        'page_obj': page_obj,
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
