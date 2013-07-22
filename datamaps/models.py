from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db import models


class World(models.Model):
    topo = models.TextField(blank=True)
    color = models.CharField(max_length=8, default='#EDDC4E')


class Scope(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    slug = models.SlugField(editable=True)
    topo = models.TextField(blank=True, editable=False)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    scale = models.DecimalField(default=0, max_digits=12, decimal_places=8)
    color = models.CharField(max_length=8, default='#EDDC4E')


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("datamaps_scope_detail", kwargs={"slug": self.slug})

    def get_topo_url(self):
        """"Return a url for where the TopoJson file for this country is."""""
        url = "{static}datamaps/scopes/{code}.json".format(
            static=settings.STATIC_URL, code=self.code)
        return url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Scope, self).save(*args, **kwargs)


class Country(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=40)
    slug = models.SlugField(editable=True)
    scope = models.ForeignKey(Scope, null=True, blank=True)
    topo = models.TextField(blank=True, editable=False)
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    radius = models.PositiveIntegerField(default=10)
    color = models.CharField(max_length=8, default='#EDDC4E')


    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("datamaps_country_detail", kwargs={"slug": self.slug})

    def get_topo_url(self):
        "Return a url for where the TopoJson file for this country is."
        url = "{static}datamaps/countries/{code}.json".format(
            static=settings.STATIC_URL, code=self.code)
        return url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)
