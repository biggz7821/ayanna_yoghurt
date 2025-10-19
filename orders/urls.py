from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_order, name='customer_order'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    
    # Using /manage/ URLs
    path('manage/', views.admin_login, name='admin_login'),
    path('manage/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage/update-order/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('manage/delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('manage/logout/', views.admin_logout, name='admin_logout'),
]