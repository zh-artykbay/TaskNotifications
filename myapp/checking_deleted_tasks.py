from datetime import datetime
from .models import Task
from django.core.mail import send_mail

def notify_assigner():
    now = datetime.now()
    tasks = Task.objects.all()

    for task in tasks:
        if now >= task.started and task.status == 1:
            send_mail('Notification', 'You need to start task',
                      'your@gmail.com',[task.assigned], fail_silently=False)
        elif now >= task.completed and task.status != 4:
            send_mail('Notification', 'You need to complete task',
                      'your@gmail.com',[task.assigned], fail_silently=False)