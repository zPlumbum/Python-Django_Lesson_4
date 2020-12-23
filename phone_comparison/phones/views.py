from django.shortcuts import render
from phones.models import Phone, Brand


def show_catalog(request):
    template = 'catalog.html'

    phones_query = Phone.objects.select_related('brand')
    print(phones_query[0].brand)

    phones_list = []
    for phone in phones_query:
        phones_list.append(
            {
                'name': phone.name,
                'price': phone.price,
                'SIM_count': phone.SIM_count,
                'OS_type': phone.OS_type,
                'resolution': phone.resolution,
                'manufacturer': phone.manufacturer,
                'brand': phone.brand,
                'double_camera': phone.double_camera,
                'headphones_port': phone.headphones_port,
                'features': phone.brand.features
            }
        )

    phone_headers = [
        "Модель",
        "Цена",
        "Количество симок",
        "Операционная система",
        "Разрешение",
        "Производитель",
        "Бренд",
        "Двойная камера",
        "Разъем под наушники",
        "Дополнения"
    ]

    context = {
        'phone_headers': phone_headers,
        'phones': phones_list
    }

    return render(request, template, context)
