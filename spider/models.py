from django.db import models

# Create your models here.


class Continent(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Country(models.Model):

    continent = models.ForeignKey(Continent)
    name = models.CharField(max_length=64)
    a2code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class SourceLinks(models.Model):

    country = models.ForeignKey(Country)
    site_name = models.CharField(max_length=128)
    url = models.URLField()

    def __str__(self):
        return self.site_name
