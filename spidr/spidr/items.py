# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from jobhuntr.search.models import JobsData


class JobDataItem(DjangoItem):
    django_model = JobsData
