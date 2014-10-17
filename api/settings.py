"""
Django settings for api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
	from getpass import getuser
	import pwd
except ImportError:
	def getuser():
		return os.environ.get('USERNAME', os.environ.get('USER'))
USER = getuser()

ADMINS = (
	('Sean', 'sean@emrals.com'),
	('Juan', 'juansantiago.medina@gmail.com')
)

MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c+o&z*%)msy5rhw*_%)y5+y8tazpbj&_0zs1^i*b(+48@$tilq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'api/templates'),
)

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'storages',
	'ecan'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.request",
	"django.core.context_processors.static",
	"django.contrib.auth.context_processors.auth",
	"django.contrib.messages.context_processors.messages",
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

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


if USER =='JuanSantiagoMedina':
	DEBUG = False
	DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'ecan_recognition',
		'USER': 'admin',
		'PASSWORD': 'admin',
		'HOST': '127.0.0.1',
		'PORT': '',
		}
	}

if USER != 'JuanSantiagoMedina':
	DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}
	DEBUG = False
	DATABASES['default'] =  dj_database_url.config()
	GS_ACCESS_KEY_ID = "GOOGBNGARUE72UFMSGKP"
	GS_SECRET_ACCESS_KEY = 'JPfZ2IxvnE1q2eGi/bTeuUlHRqSuYN+j0zI1o38t'
	GS_BUCKET_NAME = 'emfiles'
	DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
	GS_QUERYSTRING_AUTH = False



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_URL = '/media/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'app22474969@heroku.com'
EMAIL_HOST_PASSWORD = 'cpdakhlx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

#
# Google Drive Storage Settings
#

# GOOGLE_DRIVE_STORAGE = {
#     'service_account':{
#         'email': '834513284060-dd4jciar26shkhahnkbai8ltb4rn5cfd@developer.gserviceaccount.com',
#         'private_key_file_path': 'drive_api/Ecan Recognition-e6c0dad10847.p12',
#     }
# }