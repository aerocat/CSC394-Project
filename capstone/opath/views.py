from django.shortcuts import render, render_to_response
from coursesDB.models import Courses
from .forms import classroom
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request):
    form = classroom(request.GET)
    if form.is_valid():
        elective = form.cleaned_data['Electives']
        Classes = form.cleaned_data['Classes']
        Grad = form.cleaned_data['Grad']
        Time = form.cleaned_data['Time']
        return render(request, 'searchA.html', {'elective': elective, 'Classes': Classes, 'Grad':Grad, 'Time':Time})
    else:
        form = classroom()
    data = Courses.objects.order_by('course_number')
    return render(request, 'opath.html', {'data': data, 'form': form})

def PageObjects(request):
    answer = request.GET['droppdown']
    print(answer)
