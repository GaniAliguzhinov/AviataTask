celery -A Calendar worker --concurrency=4 --loglevel=info &
celery -A Calendar beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
