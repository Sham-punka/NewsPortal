from django.apps import AppConfig
import redis


red = redis.Redis(
    host='127.0.0.1',
    port='6379',

)


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals