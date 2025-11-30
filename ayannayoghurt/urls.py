from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__fix_admin__/', fix_admin),  # TEMPORARY FIX URL
    path('', include('orders.urls')),
]
