from django.db import models

# Create your models here.

class Logs(models.Model):
    user = models.CharField(max_length=200)
    ipaddr = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'users'

