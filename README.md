# Celery with Django/redis

- ~/webdev/projects/celerywithdjango/celery_with_django$

```bash
celery -A django_celery_project.celery worker -l info
```

```bash
celery -A django_celery_project.celery worker --pool=solo -l info
```

when we run the default route now, we can see that its not django that is processing the request, but celery.

### STATUS OF SCHEDULED TASKS

To check on the status of the tasks:

- create a supersuser
- go to the admin page
- click on the tasks tab
- click on the task that you want to check on

- **if you are using redis as the result backend, you can check the status of the tasks by running the following command:**

```bash
redis-cli
keys *
get <task_id>
```

## CELERY BEAT

celery beat is used to schedule/priority tasks for a later time. It is a scheduler that runs tasks at regular intervals. It is a separate service that runs alongside the worker.

- ~/webdev/projects/celerywithdjango/celery_with_django$

```bash
celery -A django_celery_project.celery beat -l info
```
