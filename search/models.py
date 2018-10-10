from django.db import models


class Continent(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Country(models.Model):

    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    a2code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class SourceLinks(models.Model):

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=128)
    url = models.URLField()  # RSS/Atom Feed

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Source Links"


class JobsData(models.Model):

    source = models.ForeignKey(SourceLinks, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # # Job URL
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Jobs Data"
