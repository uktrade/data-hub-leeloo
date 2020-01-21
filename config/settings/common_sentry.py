import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk import serializer

from config.settings.common import *

# Monkeypatch the constant that trims data in `extra`
MAX_DATABAG_BREADTH = 1000

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] [%(name)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

sentry_sdk.init(
    dsn=env('DJANGO_SENTRY_DSN'),
    environment=env('SENTRY_ENVIRONMENT'),
    integrations=[
        CeleryIntegration(),
        DjangoIntegration(),
    ],
    in_app_include=['datahub'],
)
