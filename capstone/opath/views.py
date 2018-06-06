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
        class1 = form.cleaned_data['First']
        class2 = form.cleaned_data['Second']
        online = form.cleaned_data['Online']
        credit = form.cleaned_data['Credits']
        quart = form.cleaned_data['Quarter']
        schedule = form.cleaned_data['Schedule']
        return render(request, 'searchA.html', {'schedule': schedule, 'class1': class1, 'class2': class2,
                                                'online':online, 'credit': credit, 'quart': quart})
    else:
        form = classroom()
    data = Courses.objects.order_by('course_number')
    return render(request, 'opath.html', {'data': data, 'form': form})

def PageObjects(request):
    answer = request.GET['droppdown']
    print(answer)
