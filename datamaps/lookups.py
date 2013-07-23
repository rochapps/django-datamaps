from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Country


class CountryLookup(ModelLookup):
    model = Country
    search_fields = ('name__icontains',)

registry.register(CountryLookup)