from django.contrib import admin

from .models import Country, Scope


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'scope', 'color', 'lat', 'lon', )
    list_per_page = 10
    search_fields = ["name", "code"]


admin.site.register(Country, CountryAdmin)
admin.site.register(Scope)
