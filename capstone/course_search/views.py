# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

def courseSearch(request):
	return render(request, 'course_search/course_search.html')