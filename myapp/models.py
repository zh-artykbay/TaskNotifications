from django.db import models
from django.utils.translation import ugettext_lazy as _

class Task(models.Model):

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    assigned = models.CharField(max_length=100)
    trackers = models.CharField(max_length=500)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    started = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    planned_due_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class TaskStatusHistory(models.Model):
    user = models.CharField(max_length=100)
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)
    previouse_status = models.SmallIntegerField()
    next_status = models.SmallIntegerField()
    time = models.DateTimeField(auto_now=True)
