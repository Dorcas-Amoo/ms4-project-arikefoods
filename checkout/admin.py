from django.contrib import admin
from .models import OrderDetails, OrderLineItem

"""
Credits to Codewouter's MS4 project and CI's Boutique Ado.
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(OrderDetails, OrderAdmin)
