import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'Vqivz0M11gvvKcM3klTIwTnkNn8BZvJIXQEKYGhHLEp3c0at5Xhere'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use the SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the database file
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurants',
    'users',  # Make sure this line is present
    'crispy_forms',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Global templates directory (if you have one)
            os.path.join(BASE_DIR, 'users', 'templates'),  # Add users app templates directory
            os.path.join(BASE_DIR, 'restaurants', 'templates'),  # Add restaurants app templates directory
            ],
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'users.CustomUser'  # Make sure this line is present

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] 
ROOT_URLCONF = 'atlantafoodfinder.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_MAPS_API_KEY = 'AIzaSyBLZxDKEynXZdwnrfwiLvi6UjkOew7i8-Y'
GOOGLE_PLACES_API_KEY = os.getenv('AIzaSyDybEBTmKfVLpRvWEjxzDp6rstLh_IQAvE')

