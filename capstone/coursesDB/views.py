from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from coursesDB.dataManipulationAndPopulatingDatabase.databaseRetrieval import get_course_description

def index(request):
    return HttpResponse(get_course_description("SE433"))