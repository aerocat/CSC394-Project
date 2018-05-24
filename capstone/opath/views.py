from django.shortcuts import render, render_to_response
from coursesDB.models import Courses
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request):
    data = Courses.objects.order_by('course_number')
    return render(request, 'opath.html', {'data': data})
