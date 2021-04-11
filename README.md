# TaskNotifications

TaskNotifications is feature for TrackerTask app

## Usage

-run redis
-run project
-run Celery with: celery -A tasksapp beat -l INFO and celery -A tasksapp worker -l INFO
-check requests with Postman
