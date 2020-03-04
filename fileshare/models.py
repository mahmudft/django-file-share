import os
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
def user_directory(instance, filename):
    return '{0}/{1}'.format(instance.author.username, filename)


class Upload(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=900)
    file = models.FileField(upload_to=user_directory)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('justview_upload', 'JustView upload'),
            ('fullview_upload', 'FullView upload')
        )

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Upload, self).delete(*args, **kwargs)

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_id = models.ForeignKey(Upload, default=None, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)

