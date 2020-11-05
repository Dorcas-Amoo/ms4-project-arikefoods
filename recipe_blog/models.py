from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu

# Create your models here.

""" Credits to CI's Boutique Ado Tutorial """


class RecipePost(models.Model):
    """
    This model stores each blog post details
    """
    menu = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.menu) + ' | ' + str(self.author)
