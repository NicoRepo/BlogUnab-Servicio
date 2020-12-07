from .settings import *
import os


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
STATIC_ROOT="/BlogUnab-Servicio/static"
ADMIN_ENABLED=True
DEBUG=False
SECRET_KEY=os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True

INSTALLED_APPS += ('corsheaders',)
MIDDLEWARE += ('corsheaders.middleware.CorsMiddleware',)
CORS_ORIGIN_ALLOW_ALL = True