from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django built-in admin
    path('', include('orders.urls')),  # Your custom URLs (customer + manage)
]