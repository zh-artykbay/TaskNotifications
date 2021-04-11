from rest_framework import serializers
from .models import Task, TaskStatusHistory

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "description", "assigned", "trackers", "status", "started", "completed", "planned_due_time"]

class TaskStatusHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskStatusHistory
        fields = ["user", "task", "previouse_status", "next_status"]