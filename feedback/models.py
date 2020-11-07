from django.db import models
from menu.models import Menu

# Create your models here.


class Feedback(models.Model):
    """
    This model stores comments
    """
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=254, blank=False, default='')
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
