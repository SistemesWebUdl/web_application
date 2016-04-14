from __future__ import unicode_literals

from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Country(models.Model):
    name = models.CharField(max_length=40)


class Company(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    # country = models.ForeignKey(Country, default=1)


class Actor(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField()
    deathday = models.DateField(blank=True, null=True)
    # country = models.ForeignKey(Country, default=1)
    url = models.URLField(blank=True, null=True)


class Movie(models.Model):
    name = models.CharField(max_length=40)
    movie_release_date = models.DateField(default=date.today)
    description = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    # companies = models.ManyToManyField(Company)
    # countries = models.ManyToManyField(Country, default=1)
    # actors =  models.ManyToManyField(Actor)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('movies:movie_detail', kwargs={'pk': self.pk,
                                                      'extension': 'html', })


class Director(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField(default=date.today)
    deathday = models.DateField(blank=True, null=True)
    # country = models.ForeignKey(Country, default=1)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    movies = models.ManyToManyField(Movie, related_name='directors')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('movies:director_detail', kwargs={'pk': self.pk,
                                                         'extension': 'html', })