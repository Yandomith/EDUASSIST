from .base import *

SECRET_KEY = ''

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}

STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

