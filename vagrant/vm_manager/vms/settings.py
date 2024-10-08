CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Если используете Redis
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'