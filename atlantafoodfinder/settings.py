INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurants',
    'users',
    'crispy_forms',
]

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'