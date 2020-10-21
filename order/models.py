from django.db import models


class Order(models.Model):
    """
    This model stores each order details
    """
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
