from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']

STATIC_ROOT = BASE_DIR / 'staticfiles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
