from django.db import models

# Create your models here.
class Notification(models.Model):
    # notification date
    ndate = models.DateTimeField('date time of notification')
    # nid
    nid = models.Index
