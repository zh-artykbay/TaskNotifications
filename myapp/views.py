from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task, TaskStatusHistory
from .serializers import TaskSerializer, TaskStatusHistorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core.mail import send_mail
from smtplib import SMTPException


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    if request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_status_update(request, pk, changed_status):
    if request.method == 'PUT':
        try:
            # Extract task from db
            task = Task.objects.get(id=pk)

            # Update task
            previouse_status = task.status
            task.status = changed_status
            task.save()

            # Save changing history
            task_history = TaskStatusHistory(user=str(request.user), task=task,
                                             previouse_status=previouse_status, next_status=changed_status)
            task_history.save()


            # Sending massage to trackers of task about changing status of task
            try:
                send_mail('Notification', f'Task status changed from {previouse_status} to {task.status}', 'your.99@gmail.com',
                      [email for email in task.trackers.split()], fail_silently=False)
            except SMTPException as e:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return Response(status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response(status=404)


