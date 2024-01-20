from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # id увеличивается автоматически в соответствии с доступными идентификаторами
    name = 'blog_app'
