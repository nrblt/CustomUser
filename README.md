# Creating Custom User in Django


In settings.py
AUTH_USER_MODEL = 'users.Account'

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)
