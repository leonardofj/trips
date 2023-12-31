from django.contrib import admin
from .models import Country, City, Stop, Trip


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "continent", "currency", "language", "visited")
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "lat", "lon", "state")
    search_fields = ["name"]
    autocomplete_fields = ["country"]


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ("city", "arrival", "departure", "trip")
    autocomplete_fields = ["city", "trip"]


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end", "duration"]
    search_fields = ["title"]
