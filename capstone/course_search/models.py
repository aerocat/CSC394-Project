# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    class_code = models.CharField(max_length = 10, null=True)
    class_title = models.CharField(max_length = 150, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return (self.class_code + ' - ' + self.class_title)
