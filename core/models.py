from django.db import models
from django.db.models.fields import AutoField

class TimeStampModel(models.Model):
    
    """ TimeStampModel Definition """

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        abstract = True