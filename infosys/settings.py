from pathlib import Path
import os
from dotenv import load_dotenv
import ssl

# ---------------------------
# Base directory
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv(BASE_DIR / '.env')

# ---------------------------
# Security
# ---------------------------
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ---------------------------
# Installed apps
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'ui',
    'widget_tweaks',
    'django_celery_results',  # For Celery database backend
]

# ---------------------------
# Middleware
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------
# URL Configuration
# ---------------------------
ROOT_URLCONF = 'infosys.urls'

# ---------------------------
# Templates
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'ui' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ui.context_processors.high_completion_alerts',
            ],
        },
    },
]

# ---------------------------
# WSGI
# ---------------------------
WSGI_APPLICATION = 'infosys.wsgi.application'

# ---------------------------
# Database (MySQL)
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# ---------------------------
# Custom user model
# ---------------------------
AUTH_USER_MODEL = 'ui.BaseUser'

# ---------------------------
# Password validation
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
# Internationalization
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------------
# Static & Media
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'ui' / 'static']
os.makedirs(BASE_DIR / 'ui' / 'static', exist_ok=True)
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
os.makedirs(MEDIA_ROOT, exist_ok=True)

# ---------------------------
# Default primary key field type
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------
# Login/Redirect
# ---------------------------
LOGIN_URL = 'student_login'
LOGIN_REDIRECT_URL = 'student_dashboard'
LOGOUT_REDIRECT_URL = 'home'

# ---------------------------
# Session & Security
# ---------------------------
SESSION_COOKIE_AGE = 1209600
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# ---------------------------
# Email Configuration
# ---------------------------
EMAIL_BACKEND = 'ui.email_backend.CustomEmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
SITE_URL = 'http://localhost:8000'

# Avoid SSL verification (optional for local dev)
ssl._create_default_https_context = ssl._create_unverified_context

# ---------------------------
# Notification Settings
# ---------------------------
COURSE_NOTIFICATION_TIMES = ['morning', 'afternoon', 'evening']
COURSE_COMPLETION_THRESHOLD = 75
NOTIFICATION_TIME_SLOTS = {
    'morning': '08:00',
    'afternoon': '13:00',
    'evening': '18:00'
}

# ---------------------------
# Celery Configuration
# ---------------------------
CELERY_BROKER_URL = 'django-db://'
CELERY_RESULT_BACKEND = 'django-db://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERY_BEAT_SCHEDULE = {
    'send-morning-reminders': {
        'task': 'ui.tasks.send_morning_reminders',
        'schedule': 60.0,
    },
    'send-afternoon-reminders': {
        'task': 'ui.tasks.send_afternoon_reminders',
        'schedule': 60.0,
    },
    'send-evening-reminders': {
        'task': 'ui.tasks.send_evening_reminders',
        'schedule': 60.0,
    },
    'send-daily-quiz-reminders': {
        'task': 'ui.tasks.send_daily_quiz_reminders_task',
        'schedule': 86400.0,
    },
    'send-weekly-quiz-summary': {
        'task': 'ui.tasks.send_weekly_quiz_summary_task',
        'schedule': 604800.0,
    },
}
