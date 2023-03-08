from celery import shared_task
from .utils import sync_db

@shared_task
def sync_jobs():
    sync_db()
