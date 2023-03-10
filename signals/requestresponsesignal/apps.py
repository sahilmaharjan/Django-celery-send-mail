from django.apps import AppConfig


class RequestresponsesignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'requestresponsesignal'

    def ready(self):
        import requestresponsesignal.signals
