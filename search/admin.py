from django.contrib import admin

import watson

from .models import (
    Continent,
    Country,
    SourceLinks,
    JobsData
)


@admin.register(Continent)
class GenericAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_filter = ('continent__name',)

@admin.register(SourceLinks)
class SourceLinksAdmin(admin.ModelAdmin):
    list_filter = ('country__name',)

@admin.register(JobsData)
class JobsDataAdmin(watson.admin.SearchAdmin):
    list_filter = ('source', 'source__country__name', 'added_on')
    search_fields = ('title',)
