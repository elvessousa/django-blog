from django.db import models
from datetime import datetime
from django_quill.fields import QuillField

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = QuillField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
