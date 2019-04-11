from django.apps import AppConfig


class WebappConfig(AppConfig):
    name = 'WebApp'
    def ready(self):
        import WebApp.signals
