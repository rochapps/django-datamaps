"""
    You should not need this urls in your project. The are meant only as an
    example. Do not use them in your project, unless you really want to!
"""
from django.conf.urls import patterns, url
from django.views.generic import ListView

from datamaps.models import Country, Scope
from .views import ScopeDetailView, CountryListView, CountryDetailView


urlpatterns = patterns('',
    url(r'^countries/$', CountryListView.as_view(
        model = Country
        ), name='datamaps_country_list'),
    url(r'^countries/(?P<slug>[-\w]+)/$', CountryDetailView.as_view(
        model = Country
        ), name='datamaps_country_detail'),
    url(r'^scopes/$', ListView.as_view(
        model = Scope
        ), name='datamaps_scope_list'),
    url(r'^scopes/(?P<slug>[-\w]+)/$', ScopeDetailView.as_view(
        model = Scope
        ), name='datamaps_scope_detail'),
    url(r'^$', ListView.as_view(
        model = Scope,
        template_name="datamaps/maps.html"
        ), name='datamaps_scope_maps'),
)
