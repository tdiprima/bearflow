"""
Celery distributed task queue implementation using Redis broker.

Defines two asynchronous tasks (task_a, task_b) that can be executed by Celery workers.
Start worker: celery -A celery_den worker --loglevel=info
Execute tasks: task_a.delay(); task_b.delay()
"""

# ⚙️  Celery
from celery import Celery

app = Celery("bearflow", broker="redis://localhost:6379/0")


@app.task
def task_a():
    print("Celery: Task A complete")


@app.task
def task_b():
    print("Celery: Task B complete")


# To run this POC:
#   celery -A celery_den worker --loglevel=info
# Then, in another shell:
#   from celery_den import task_a, task_b
#   task_a.delay(); task_b.delay()
