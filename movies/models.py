from __future__ import unicode_literals

from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class City(models.Model):
    city_name = models.CharField(max_length=40)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.city_name

    def get_absolute_url(self):
        return reverse('movies:city_detail', kwargs={'pk': self.pk,
                                                        'extension': 'html', })

class Actor(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, default=1)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="movie", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('movies:actor_detail', kwargs={'pk': self.pk,
                                                      'extension': 'html', })


class Director(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="movie", blank=True, null=True)


    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('movies:director_detail', kwargs={'pk': self.pk, 'extension': 'html', })


class Company(models.Model):
    company_name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.company_name

    def get_absolute_url(self):
        return reverse('movies:company_detail', kwargs={'pk': self.pk,
                                                        'extension': 'html', })


class Movie(models.Model):
    movie_name = models.CharField(max_length=40)
    movie_release_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    cities = models.ManyToManyField(City, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    companies = models.ManyToManyField(Company, blank=True)
    image = models.ImageField(upload_to="movie", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.movie_name

    def get_absolute_url(self):
        return reverse('movies:movie_detail', kwargs={'pk': self.pk,
                                                      'extension': 'html', })
