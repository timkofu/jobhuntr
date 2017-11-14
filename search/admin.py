from django.contrib import admin

from daterange_filter.filter import DateRangeFilter

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
class JobsDataAdmin(admin.ModelAdmin):
    # #list_display = ('title', 'source')
    list_filter = (
        'source__country',
        'source__site_name',
        ('added_on', DateRangeFilter),
    )
    search_fields = ('title',)
