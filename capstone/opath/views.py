from django.shortcuts import render, render_to_response
from coursesDB.models import Courses
from .forms import classroom
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from coursesDB.dataManipulationAndPopulatingDatabase.efficientCourseAlgorithm import have_prereqs_for_electives
# Create your views here.

@login_required(login_url="/accounts/login/")
def index(request):
    form = classroom(request.GET)
    if form.is_valid():
        elective = return_concentration(int(form.cleaned_data['Electives']))
        Classes = form.cleaned_data['Classes']
        Grad = form.cleaned_data['Grad']
        Time = form.cleaned_data['Time']
        if(bool(Grad)):
            text = "currently a graduate"
        else:
            text = "currently a undergraduate"
        return render(request, 'searchA.html', {'elective': elective, 'Classes': Classes, 'text':text, 'Time':Time})
    else:
        form = classroom()
    data = Courses.objects.order_by('course_number')
    return render(request, 'opath.html', {'data': data, 'form': form})

def return_concentration(conc_int):
    global elective_preference
    if(conc_int == 1):
        elective_preference = "software systems"
    elif(conc_int == 2):
        elective_preference = "data science"
    elif(conc_int == 3):
        elective_preference = "database systems"
    elif(conc_int == 4):
        elective_preference = "artificial intelligence"
    elif(conc_int == 5):
        elective_preference = "software engineering"
    elif(conc_int == 6):
        elective_preference = "game and real time systems"
    elif(conc_int == 7):
        elective_preference = "software engineering"
    return elective_preference

def PageObjects(request):
    answer = request.GET['droppdown']
    print(answer)
