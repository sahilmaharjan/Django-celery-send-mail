from django.apps import AppConfig


class ModelsignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modelsignal'

    def ready(self):
        import modelsignal.signals