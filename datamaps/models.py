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
    scale = models.FloatField(default=0)
    color = models.CharField(max_length=8, default='#EDDC4E')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("datamaps_scope_detail", kwargs={"slug": self.slug})

    def json_serializable(self):
        """Serializes current instance"""
        data = {"code": self.code, "name": self.name, "lat": float(self.lat),
                "lon": float(self.lon), "scale": float(self.scale),
                "color": self.color}
        return data

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

    def json_serializable(self):
        """Serializes current instance"""
        data = {"code": self.code, "name": self.name, "lat": float(self.lat),
                "lon": float(self.lon), "scale": float(self.scale),
                "color": self.color}

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)
