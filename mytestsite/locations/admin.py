from django.contrib import admin
from .models import Symbol, Country, City

# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_filter = ['country']


admin.site.register(Symbol)