import os

from prettyconf import config


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG")
ALLOWED_HOSTS = config("ALLOWED_HOSTS")

# Application definition
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "listings_api",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "listingsapi.urls"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "listings_api.utils.custom_exception_handler.custom_exception_handler"
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "listingsapi.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

LISTINGS_URL = "http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json"

ZAP_BBOX_MIN_LATITUDE = config("ZAP_BBOX_MIN_LATITUDE")

ZAP_BBOX_MIN_LONGITUDE = config("ZAP_BBOX_MIN_LONGITUDE")

ZAP_BBOX_MAX_LATITUDE = config("ZAP_BBOX_MAX_LATITUDE")

ZAP_BBOX_MAX_LONGITUDE = config("ZAP_BBOX_MAX_LONGITUDE")

ZAP_MIN_SALE_PRICE = int(config("ZAP_MIN_SALE_PRICE"))
ZAP_MIN_RENTAL_PRICE = int(config("ZAP_MIN_RENTAL_PRICE"))
VIVAREAL_MAX_SALE_PRICE = int(config("VIVAREAL_MAX_SALE_PRICE"))
VIVAREAL_MAX_RENTAL_PRICE = int(config("VIVAREAL_MAX_RENTAL_PRICE"))

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
