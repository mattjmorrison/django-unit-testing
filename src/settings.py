from os import path
DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = path.abspath(path.dirname(__file__))

ADMINS = (
    ('Matthew J. Morrison', 'mattj.morrison@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.database',
    }
}

USE_I18N = False
USE_L10N = True
MEDIA_ROOT = path.join(PROJECT_DIR, 'media')
STATIC_ROOT = MEDIA_ROOT
MEDIA_URL = '/static/'
SECRET_KEY = '-2cmgs7l$5grqwd!x&6241^ah&xx34ki48fwn#ef5s_lm(1@0a4w&v'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'src.urls'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'south',
    'debug_toolbar',
    'django_testing',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    'INTERCEPT_REDIRECTS': False,
}

MASHER_COMPRESS = True

# Test settings
SOUTH_TESTS_MIGRATE = False
TEST_RUNNER = 'django_testing.TestSuiteRunner'
TEST_OUTPUT_VERBOSE = False
TEST_OUTPUT_DESCRIPTIONS = False
TEST_OUTPUT_DIR = 'xmlrunner'
