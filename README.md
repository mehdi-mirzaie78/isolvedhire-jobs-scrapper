# isolvedhire-jobs-scrapper


## celery beat

in this directory: 
    $ isolvedhire-jobs-scrapper\isolvehire_jobs_scrapper_django

run celery:
    $ celery -A config worker -l INFO

run celery beat:
    $ celery -A config beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
