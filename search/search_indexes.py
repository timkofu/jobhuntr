
import datetime

from haystack import indexes
from .models import JobsData


class JobsDataIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    added_on = indexes.DateTimeField(model_attr='added_on')
    
    def get_model(self):
        return JobsData
    
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            added_on__gte=(datetime.datetime.now() - datetime.timedelta(days=28))
        )
