ADMINS = (
    ('Tim', 'xxvii.x@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database-name',
        'USER': 'database-username',
        'PASSWORD': 'database-password',
        'HOST': 'database-host-if-any',
        'PORT': 'database-port-if-any',
    }
}

TIME_ZONE = 'America/Toronto'

SECRET_KEY = 'your-random-secret-key-here'

