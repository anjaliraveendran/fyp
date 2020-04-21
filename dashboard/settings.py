import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print( '******* BaseDir {}'.format( BASE_DIR ) )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+-g0!o^oa^%o=y)-5gk_m(@m(0#*f5f4gqk_!*rtc774(jqc24'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'landingpage',
    'home',
    'crispy_forms',
    'leaflet',
    'djgeojson',
    'django_plotly_dash.apps.DjangoPlotlyDashConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_plotly_dash.middleware.BaseMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'


ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #add extra templates here:
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'dashboard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'avianinfluenza',
        'USER': 'sample_user',
        'PASSWORD': 'sample_password',
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
                    'NAME': 'testDB',
                }
    }
}

DATE_INPUT_FORMATS = ['%d-%m-%Y']


SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK='bootstrap4'

ASGI_APPLICATION = 'dashboard.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG':{
            'hosts': [('127.0.0.1', 6379),],
        }
    }
}

STATICFILES_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder'
]

PLOTLY_COMPONENTS = {
    'dash_core_components',
    'dash_html_components',
    'dash_renderer',
    'dpd_components'
}

PLOTLY_DASH = {'cache_arguments': False}

STATIC_URL = '/static/'

STATICFILES_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dashboard/static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-.023, 36.87),
    'DEFAULT_ZOOM':2,
    'MAX_ZOOM': 20,
    'MIN_ZOOM':3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX':'AVIAN INFLUENZA DASHBOARD',
    'TILES': [('OpenStreet Map', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>', 'maxZoom':20}),
              ('Terrain Map', 'http://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Copyright:© 2013 ESRI, i-cubed, GeoEye','maxZoom': 16}),
              ('Data Map', 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {'attribution':'Map tiles by Carto, under CC BY 3.0. Data by OpenStreetMap, under ODbL'})]
}

LOGIN_REDIRECT_URL = "user_home"
LOGOUT_REDIRECT_URL = "dashboard_welcome"
LOGIN_URL = "user_login"
LOGOUT_URL = "user_logout"
