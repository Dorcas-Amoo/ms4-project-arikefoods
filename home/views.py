from django.shortcuts import render

# Create your views here.

""" Credits to CI's Boutique Ado Tutorial """


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact_us(request):
    """ A view to return the contact page """

    return render(request, 'home/contact.html')
