from django.contrib import admin

from models import (
    Continent,
    Country,
    SourceLinks,
    JobsData
)


@admin.register(Continent, Country, SourceLinks, JobsData)
class GenericAdmin(admin.ModelAdmin):
    pass
