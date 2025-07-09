from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('DISPATCHED', 'Dispatched'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product} ({self.delivery_status})"
