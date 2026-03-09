# users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  # 如果你把訊號寫在單獨的 signals.py
        # 或者如果你寫在 models.py，就確保 models 被載入