from timeit import default_timer
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Product

# Create your views here.
def shop_index(requst: HttpRequest):
    products = [
        ('Negr', 1000),
        ('Pizda', 9494),
        ('Bubna', 44444),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    
    return render(requst, 'shopapp/shopindex.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, "shopapp/products-list.html", context=context)