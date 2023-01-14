from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from kipikshopbckend import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
