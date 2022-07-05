import os
from django.apps import AppConfig
# from .bot import main

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    # def ready(self):
    #     if os.environ.get('RUN_MAIN', None) != 'true':
    #         main()
