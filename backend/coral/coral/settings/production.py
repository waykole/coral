from .base import *

DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),  # noqa
        'KEY_PREFIX': 'coral',
        'TIMEOUT': 14400,  # in seconds
    }
}

try:
    from .local import *
except ImportError:
    pass
