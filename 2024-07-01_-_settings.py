# python3 manage.py collectstatic #1:

#my_project/project/settings.py: #5:
DEBUG = False #2:

ALLOWED_HOSTS = [ #3:
    '127.0.0.1'
]
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'base' / 'static'
]
STATIC_ROOT = BASE_DIR / 'static_files' #4:

#pip install whitenoise
