from django.db import models

# Create your models here.


class Courses(models.Model):
    course_json = models.TextField()
    course_number = models.TextField()

    def __unicode__(self):
        return self.course_number

