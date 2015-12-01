
import datetime

from haystack import indexes
from .models import JobsData


class JobDataIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    add_time = indexes.DateTimeField(model_attr='add_time')
    
    def get_model(self):
        return JobsData
    
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(added_on__gte=(datetime.datetime.now() - datetime.timedelta(days=28)))
