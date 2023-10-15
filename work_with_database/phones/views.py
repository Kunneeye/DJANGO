from django.shortcuts import render, redirect
from phones.models import Phone
from operator import attrgetter

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort = request.GET.get("sort")
    if not sort is None:
        if sort.endswith('price'):
            phone_objects = sorted(phone_objects, key=attrgetter('price'), reverse=sort.startswith('max_price'))
        else:
            phone_objects = sorted(phone_objects, key=attrgetter(sort))
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug__contains = slug)
    for i in phone_objects:
        phone = i
    context = {
        'phone': phone
    }
    return render(request, template, context)
