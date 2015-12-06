from django.db import models


class Continent(models.Model):

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Country(models.Model):

    continent = models.ForeignKey(Continent)
    name = models.CharField(max_length=64)
    a2code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class SourceLinks(models.Model):

    country = models.ForeignKey(Country)
    site_name = models.CharField(max_length=128)
    url = models.URLField()  # RSS Jobs Feed

    def __unicode__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Source Links"


class JobsData(models.Model):

    source = models.ForeignKey(SourceLinks)
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Jobs Data"
