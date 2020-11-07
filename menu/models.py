from django.db import models

""" Credits to CI's Boutique Ado Tutorial """


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Menu(models.Model):
    """
    This model stores each menu item details
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=1024, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
