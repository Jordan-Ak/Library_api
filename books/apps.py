from django.apps import AppConfig

#This file allows the usage of signals
class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        import books.signals