from django.db import models
from django.utils import timezone

# Create your models here.

class Timecard(models.Model):
    name = models.CharField(max_length=32)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.DecimalField(decimal_places=2, max_digits=4)
    dateOfWork = models.DateField()
    dateOfEntry = models.DateTimeField()