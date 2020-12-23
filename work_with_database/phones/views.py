from pprint import pprint

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}

    sort = request.GET.get('sort')

    if sort == 'name':
        phones_query = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones_query = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones_query = Phone.objects.all().order_by('-price')
    else:
        phones_query = Phone.objects.all()

    phones = []
    for phone in phones_query:
        phones.append(
            {
                'name': phone.name,
                'price': phone.price,
                'image': phone.image,
                'release_date': phone.release_date,
                'lte_exists': phone.lte_exists,
                'slug': phone.slug
            }
        )

    context.setdefault('phones', phones)

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    try:
        phone_query = Phone.objects.all().filter(slug=slug)
        print(phone_query)
        context = {
            'phone': {
                'name': phone_query[0].name,
                'price': phone_query[0].price,
                'image': phone_query[0].image,
                'release_date': phone_query[0].release_date,
                'lte_exists': phone_query[0].lte_exists
            }
        }
    except Exception as ex:
        print(ex)
        print('Такой модели нет на сайте.')
        context = {
            'phone': None
        }

    return render(request, template, context)
