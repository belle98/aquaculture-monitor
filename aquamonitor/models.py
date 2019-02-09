from django.conf import settings
from django.db import models
from django.utils import timezone


class Data(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    oxygen = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    humidity = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created_date