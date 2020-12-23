from django.contrib import admin
from phones.models import Phone, Brand


class PhoneAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Brand, BrandAdmin)
