from django.apps import AppConfig


class ObraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'obra'
    verbose_name = 'Perfiles'

    def ready(self):
        import obra.signals
