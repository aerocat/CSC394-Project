from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Q

import json

# Create your views here.
from .models import Courses

def index(request):
    course = Courses.objects.get(course_number="MGT500")
    course_dictionary = json.loads(course.course_json)
    return render(request, 'coursesDB/single_course.html', {'course': course_dictionary})

def get_courses(request, ):
    lst_of_courses = []
    query = request.GET.get('q')
    if query:
        try:
            courses_objects = Courses.objects.filter(course_number__contains = query)
            for course_object in courses_objects:
                course_dictionary = json.loads(course_object.course_json)
                lst_of_courses.append(course_dictionary)
        except:
            lst_of_courses = []
    else:
        courses_objects = Courses.objects.all()
        for course_object in courses_objects:
            course_dictionary = json.loads(course_object.course_json)
            lst_of_courses.append(course_dictionary)
    return render(request, 'coursesDB/all.html', {'lst_of_courses': lst_of_courses})

def CourseSingleView(request, course_id):
    try:
        course = Courses.objects.get(course_number=course_id)
    except:
	    return render(request, 'coursesDB/missing_course.html')
    course_dictionary = json.loads(course.course_json)
    return render(request, 'coursesDB/single_course.html', {'course': course_dictionary})