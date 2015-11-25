from django.db import models

from spider.models import SourceLinks


class JobsData(models.Model):

    source = models.ForeignKey(SourceLinks)
    title = models.CharField(max_length=255)
    url = models.URLField()
    collected_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
