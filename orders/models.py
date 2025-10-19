from django.db import models

class Order(models.Model):
    DELIVERY_TIMES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.TextField()
    delivery_time = models.CharField(max_length=20, choices=DELIVERY_TIMES)
    order_details = models.JSONField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
    
    def total_amount(self):
        total = 0
        prices = {'250ml': 50, '500ml': 100, '1L': 200}
        for item in self.order_details:
            total += prices[item['size']] * item['quantity']
        return total