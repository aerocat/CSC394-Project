from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse
from coursesDB.dataManipulationAndPopulatingDatabase.databaseRetrieval import get_course_description
from .models import Courses

def index(request):
    return HttpResponse(get_course_description("SE433"))



def get_courses(request, ):
    # course_json_Object = Courses.objects.get(course_number="CSC400")
    lst_of_courses = []
    courses_objects = Courses.objects.all()
    for course_object in courses_objects:
        course_dictionary = json.loads(course_object.course_json)
        lst_of_courses.append(course_dictionary)
    print(len(lst_of_courses))
    # course_dictionary = json.loads(course_json_Object.course_json)
    return render(request, 'coursesDB/all.html', {'lst_of_courses': lst_of_courses})
