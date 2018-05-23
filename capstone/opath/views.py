from django.shortcuts import render, render_to_response
from coursesDB.models import Courses
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = Courses.objects.order_by('course_number')
    return render(request, 'opath.html', {'data': data})