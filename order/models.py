from django.db import models
from menu.models import Menu


class Order(models.Model):
    """
    This model stores each order details
    """
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
