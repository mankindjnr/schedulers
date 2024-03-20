# you can create this file in any app folder
from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return "done"
