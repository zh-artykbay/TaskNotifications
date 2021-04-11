from celery import shared_task
from .checking_deleted_tasks import notify_assigner

@shared_task
def notify():
    return notify_assigner()