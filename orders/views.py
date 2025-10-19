from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Order

@csrf_exempt
def customer_order(request):
    print("=== ORDER VIEW CALLED ===")
    print(f"Method: {request.method}")
    
    if request.method == 'POST':
        print("=== POST REQUEST RECEIVED ===")
        try:
            # Check if it's JSON data (from AJAX)
            if request.content_type == 'application/json':
                print("Processing JSON data...")
                data = json.loads(request.body)
                print(f"JSON Data: {data}")
                
                # Validate required fields
                required_fields = ['customer_name', 'phone_number', 'location', 'delivery_time', 'order_items']
                for field in required_fields:
                    if field not in data:
                        raise ValueError(f"Missing required field: {field}")
                
                order = Order(
                    customer_name=data['customer_name'],
                    phone_number=data['phone_number'],
                    location=data['location'],
                    delivery_time=data['delivery_time'],
                    order_details=data['order_items']
                )
                order.save()
                
                print(f"✅ ORDER SAVED: #{order.id}")
                return JsonResponse({'success': True, 'order_id': order.id})
                
            else:
                # If it's a traditional form (shouldn't happen with our AJAX), redirect to prevent resubmission
                return redirect('customer_order')
            
        except Exception as e:
            print(f"❌ ERROR: {e}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'error': str(e)})
            else:
                return render(request, 'orders/customer_order.html', {'error': str(e)})
    
    # Handle GET requests - just render the page
    return render(request, 'orders/customer_order.html')

def order_success(request, order_id):
    """Display order success page"""
    try:
        order = Order.objects.get(id=order_id)
        return render(request, 'orders/order_success.html', {
            'order': order,
            'order_id': order_id,
            'customer_name': order.customer_name
        })
    except Order.DoesNotExist:
        return render(request, 'orders/order_success.html', {
            'order_id': order_id,
            'customer_name': 'Customer'
        })

@login_required
def admin_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/admin_dashboard.html', {'orders': orders})

@login_required
def update_order_status(request, order_id):
    print(f"=== UPDATE STATUS REQUEST ===")
    print(f"Order ID: {order_id}")
    print(f"Method: {request.method}")
    
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            new_status = request.POST.get('status')
            print(f"Updating order #{order_id} from '{order.status}' to '{new_status}'")
            
            order.status = new_status
            order.save()
            
            print(f"✅ STATUS UPDATED: #{order_id} -> {new_status}")
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            print(f"❌ ORDER NOT FOUND: #{order_id}")
            return JsonResponse({'success': False, 'error': 'Order not found'})
        except Exception as e:
            print(f"❌ UPDATE ERROR: {e}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    print(f"❌ INVALID METHOD: {request.method}")
    return JsonResponse({'success': False, 'error': 'Invalid method'})

@login_required
@csrf_exempt
def delete_order(request, order_id):
    print(f"=== DELETE ORDER REQUEST ===")
    print(f"Order ID: {order_id}")
    print(f"Method: {request.method}")
    print(f"User: {request.user}")
    
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            customer_name = order.customer_name
            order_details = order.order_details
            
            print(f"Found order: #{order.id} - {customer_name}")
            print(f"Order details: {order_details}")
            
            order.delete()
            print(f"✅ ORDER DELETED: #{order_id} - {customer_name}")
            return JsonResponse({'success': True, 'message': f'Order #{order_id} deleted'})
            
        except Order.DoesNotExist:
            print(f"❌ ORDER NOT FOUND: #{order_id}")
            return JsonResponse({'success': False, 'error': 'Order not found'})
        except Exception as e:
            print(f"❌ DELETE ERROR: {e}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    print(f"❌ INVALID METHOD: {request.method}")
    return JsonResponse({'success': False, 'error': 'Invalid method'})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'orders/admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'orders/admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')