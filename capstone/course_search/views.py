# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

from course_search.models import Course

class CourseListView(ListView):
	model = Course
	template_name = 'course_search/course_list.html'
	
def CourseSingleView(request, class_code_in):
	course = Course.objects.get(class_code=class_code_in)

	return HttpResponse("View for course with class code %s." % course.class_code)