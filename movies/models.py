from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
    name = models.TextField()

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    country = models.ForeignKey(Country, default=1)

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    birthday = models.DateField()
    deathday = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, default=1)
    url = models.URLField(blank=True, null=True)

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    birthday = models.DateField()
    deathday = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, default=1)
    url = models.URLField(blank=True, null=True)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    date = models.DateField()
    description = models.TextField()
    companies = models.ManyToManyField(Company)
    countries = models.ManyToManyField(Country, default=1)
    actors =  models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
