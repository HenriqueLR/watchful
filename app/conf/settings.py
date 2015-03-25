#encoding: utf-8

import os.path
VAR_ROOT = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = '!t7nb1zy*isd5wxr(lbp-g!aasju8s+8n$m(vups8-l$^3&7l7'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_toolkit',
    'seek',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'watchful.sqlite'),
    }
}


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


MEDIA_ROOT = os.path.join(VAR_ROOT,'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(VAR_ROOT,'static_files')
STATIC_URL = '/static/'

STATICFILES_DIRS = (

        os.path.join(VAR_ROOT,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
        os.path.join(VAR_ROOT,'templates'),
)


from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('controll')
LOGOUT_URL = reverse_lazy('login')

DATE_HOUR = '%Y-%m-%d %H:%M:%S.%f'
DATE_FORMAT = '%d/%m/%Y'
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')
DATETIME_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True