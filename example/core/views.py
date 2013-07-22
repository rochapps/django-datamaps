"""
    Views in this file are meant only as an example. Do not use them in
    your project, unless you really want to!
"""
import json
import random

from django.views.generic import DetailView, ListView


class ScopeDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(ScopeDetailView, self).get_context_data(**kwargs)
        scope = context['object']
        radius = [5, 8, 11, 14, 17]
        map_data = {}
        map_bombs = []
        fills = {'defaultFill': '#EDDC4E', 'country': '#1f77b4'}
        for country in scope.country_set.all():
            map_data[country.code] = {
                'name': country.name,
                'description': country.code,
                'fillKey': 'defaultFill'
            }
            bomb = {
                'name': country.name,
                'radius': random.choice(radius),
                'country': country.name,
                'fillKey': 'country',
                'significance': 'RochApps.com',
                'date': '1961-10-31',
                'latitude': country.lat,
                'longitude': country.lon
            }
            map_bombs.append(bomb)
        context.update({
            'map_data': json.dumps(map_data),
            'map_bombs': json.dumps(map_bombs),
            'fills': json.dumps(fills),
            'scope': scope,
        })
        return context


class CountryDetailView(DetailView):

    def get_context_data(self, **kwargs):
        context = super(CountryDetailView, self).get_context_data(**kwargs)
        country = context['object']
        radius = [5, 8, 11, 14, 17]
        map_bombs = []
        map_data = {}
        fills = {'defaultFill': '#EDDC4E', 'country': '#1f77b4'}
        map_data[country.code] = {
            'name': country.name,
            'description': country.code,
            'fillKey': 'defaultFill'
        }
        bomb = {
            'name': country.name,
            'radius': random.choice(radius),
            'country': country.name,
            'fillKey': 'country',
            'significance': 'RochApps.com',
            'date': '1961-10-31',
            'latitude': country.lat,
            'longitude': country.lon
        }
        map_bombs.append(bomb)
        context.update({
            'map_data': json.dumps(map_data),
            'map_bombs': json.dumps(map_bombs),
            'fills': json.dumps(fills),
            'scope': country.scope,
        })
        return context

class CountryListView(ListView):
    pass