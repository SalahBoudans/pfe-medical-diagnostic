"""
Exemple de fichier de configuration Django.

Copiez ce fichier en `PFE/settings.py` et remplacez les valeurs
placeholder par vos informations (clé secrète, email, mot de passe d'application, etc.).
NE PAS committer `PFE/settings.py` dans le dépôt public car il contient des secrets.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<YOUR_SECRET_KEY>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/login/'

# Email settings (replace with your values)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '<YOUR_EMAIL@example.com>'
EMAIL_HOST_PASSWORD = '<YOUR_EMAIL_PASSWORD_OR_APP_PASSWORD>'

# Media / Static defaults (adaptez si besoin)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Database example (adaptez selon votre environnement)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
