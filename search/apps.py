from django.apps import AppConfig

class SearchConfig(AppConfig):

    name = 'search'
    verbose_name = 'Search'

    def ready(self):
        pass
        #watson.search.register(self.get_model('JobsData'))
