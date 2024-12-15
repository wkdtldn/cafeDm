from django.db import models


class Order(models.Model):
    ORDER_CHOICES = [
        ("현금", "현금"),
        ("송금", "송금"),
        ("쿠폰", "쿠폰"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    order_by = models.CharField(max_length=10, choices=ORDER_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order {self.id} - {self.order_by}"


class Drink(models.Model):
    order = models.ForeignKey(Order, related_name="drinks", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ice = models.PositiveIntegerField(null=True, blank=True)
    hot = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} (Order {self.order.id})"
