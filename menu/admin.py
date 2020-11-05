from django.contrib import admin
from .models import Menu, Category

# Register your models here.

""" Credits to CI's Boutique Ado Tutorial """


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'price',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
