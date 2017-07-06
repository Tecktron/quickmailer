import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'Quickmailer_in_django'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INSTALLED_APPS = ()
MIDDLEWARE = ()
TEMPLATES = ()

# For email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = ''

# logging
LOG_FILE = os.environ.get('LOG_FILE', os.path.join(BASE_DIR, 'quickmail.log'))
LOGGING = {
    'version': 1,
    'formatters': {
        'basic': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'basic'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'basic'
        },
    },
    'loggers': {
        'mailer': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# This makes it so you can use a local settings file to override settings
try:
    from .local_settings import *
except ImportError:
    pass