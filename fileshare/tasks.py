from __future__ import absolute_import, unicode_literals
from datetime import datetime
from celery import shared_task
from .models import Upload

@shared_task
def file_auto_delete():
    files = Upload.objects.all()
    for file in files:
       timed = file.uploaded_at
       current_time = datetime.now()
       if (current_time - timed.strftime("%Y-%m-%d")) > 7:
           file.delete(save=True)
