from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),   # your customer order page
    # path('__fix_admin__/', fix_admin),   # ← removed
]
