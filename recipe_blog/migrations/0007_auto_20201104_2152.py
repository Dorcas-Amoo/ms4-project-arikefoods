# Generated by Django 3.1.2 on 2020-11-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_blog', '0006_auto_20201104_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepost',
            name='slug',
            field=models.SlugField(default='', max_length=254, unique=True),
        ),
    ]
