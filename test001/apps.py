from django.apps import AppConfig


class Test001Config(AppConfig):
    name = 'test001'

    def ready(self):
        import test001.signals
