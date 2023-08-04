from django.conf import settings
from django.db import models
from django.utils import timezone
from jdatetime import datetime


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def __str__(self):
        return self.title + " " + str(self.id)
