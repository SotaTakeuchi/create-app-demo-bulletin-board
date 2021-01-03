from django.db import models
import datetime

# Create your models here.
class Message(models.Model):
    """チャットの履歴保存"""
    course = models.CharField(max_length=8, default='engineer')
    user = models.CharField(max_length=256, default='NO_NAME')
    message = models.TextField(default='')
    created = models.DateTimeField(default=datetime.datetime.now)
