from django.db import models
from django.urls import reverse

from kipikshopbckend.settings import AUTH_USER_MODEL


# Category model
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Product model

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=520, unique=True)
    price = models.FloatField(default=0.00)
    # price_ttc = models.FloatField(default=0.00, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='images/store/products/', default='images/store/products/default.png', blank=True, null=True)
    stock = models.IntegerField(default=0)
    marque_produit = models.CharField(max_length=120)

    # Affiche le nom du produit
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    # TVA 20%
    def tva(self):
        return self.price * 0.2

    # Prix TTC
    def ttc_price(self):
        return self.price * 1.2



class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    code_produit = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name_plural = 'Orders'
        ordering = ('user',)



class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)

    # ordered_date = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Carts'
        ordering = ('user',)
