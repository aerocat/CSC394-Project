from django.db import models

# Create your models here.


class Coursetable(models.Model):
    coursec = models.TextField()
    coursesubject = models.TextField()
    coursenumber = models.IntegerField()

