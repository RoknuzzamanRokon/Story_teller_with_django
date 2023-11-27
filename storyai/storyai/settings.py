from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xde%&%^#yu90e^@zuj)5q!_-1%nu5f78_%esqwpd-#1ksiw=_y'

OPENAI_SECRET_KEY = os.environ.get('OPENAI_SECRET_KEY')
DEBUG=os.environ.get('DEBUG')
ALLOWED_HOSTS =os.environ.get('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'app.apps.AppConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'storyai.urls'

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

WSGI_APPLICATION = 'storyai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'story_ai_db',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST':'localhost',
        'PORT':'3306',
        }
    }


# DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'aistory',
#         'USER': 'adminarti',
#         'PASSWORD': 'Aws52701426##',
#         'HOST': 'aistory.cg9zjgvxejic.ap-southeast-1.rds.amazonaws.com',
#         'PORT':'3306',
#         }
#     }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('MYSQL_DATABASE'),
#         'USER': 'root',
#         'PASSWORD': os.environ.get('MYSQL_ROOT_PASSWORD'),
#         'HOST': 'db', 
#         'PORT': 3306,
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'" ,
#             'charset': 'utf8mb4',
#             'collation': 'utf8mb4_unicode_ci',
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ALLOWED_HOSTS = ['*']
APPEND_SLASH=False