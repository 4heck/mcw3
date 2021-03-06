import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ju6h12ev!&l_r#byfz3p57&gqamng0mh%(9zh6d6rp-y=%&%bw'

ADMIN_SITE_HEADER = "Parsing Admin Panel v3"

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '0.0.0.0'),

# ALLOWED_HOSTS = ['127.0.0.1', '134.0.117.214', 'localhost']

ALLOWED_HOSTS = ['*']

DEBUG = os.environ.get('DEBUG', True)

STATIC_URL = '/static/'

DJANGO_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'import_export'
]

LOCAL_APPS = [
    'monitoring_app.apps.MonitoringAppConfig'

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'mcw_price_monitoring.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mcw_price_monitoring.wsgi.application'

postgres = True

if postgres:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db_monitoring',
            'USER': 'monitoring_admin',
            'PASSWORD': 'password',
            # 'HOST': '0.0.0.0',
            'HOST': os.environ.get('DB_HOST', '0.0.0.0'),
            'PORT': '5432'
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'monitoring.db'),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Мониторинг цен',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,   # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    'SEARCH_URL': '/admin/monitoring_app/item/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('monitoring_app.item',),
    'MENU': (
        # 'sites',
        {'app': 'monitoring_app', 'icon': 'icon-cog', 'url': '/admin/monitoring_app/'},
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'label': 'Помощь', 'icon': 'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    'LIST_PER_PAGE': 25
}

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

#
# if DEBUG:
#     INTERNAL_IPS = ['127.0.0.1']
