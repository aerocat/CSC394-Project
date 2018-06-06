from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
# Create your views here.

from accounts.models import Faculty, Student

def index(request):
	return render(request, 'LandingPage/index.html')

@login_required(login_url="/accounts/login/")
def StudentSingleView(request, student_id_in):
	try:
		student = Student.objects.get(student_id=student_id_in)
	except:
		return render(request, 'LandingPage/missing_student.html')
	return render(request, 'LandingPage/single_student.html', {'student': student})

@login_required(login_url="/accounts/login/")
def FacultySingleView(request, faculty_id_in):
	try:
		faculty = Faculty.objects.get(faculty_id=faculty_id_in)
	except:
		return render(request, 'LandingPage/missing_faculty.html')
	return render(request, 'LandingPage/single_faculty.html', {'faculty': faculty})

@login_required(login_url="/accounts/login/")
def FacultyListView(request, ):
    faculty_list = []
    query = request.GET.get('q')
    if query:
        try:
            faculty_objects = Faculty.objects.filter(faculty_name_first__contains = query)
            for faculty_object in faculty_objects:
                faculty_list.append(faculty_object)
            faculty_objects = Faculty.objects.filter(faculty_name_last__contains = query)
            for faculty_object in faculty_objects:
                if faculty_object not in faculty_list:
                    faculty_list.append(faculty_object)
        except:
            faculty_list = []
    else:
        faculty_objects = Faculty.objects.all()
        for faculty_object in faculty_objects:
            faculty_list.append(faculty_object)
    return render(request, 'LandingPage/faculty_list.html', {'faculty_list': faculty_list})

@login_required(login_url="/accounts/login/")
def StudentListView(request, ):
    student_list = []
    query = request.GET.get('q')
    if query:
        try:
            student_objects = Student.objects.filter(student_name_first__contains = query)
            for student_object in student_objects:
                student_list.append(student_object)
            student_objects = Student.objects.filter(student_name_last__contains = query)
            for student_object in student_objects:
                if student_object not in student_list:
                    student_list.append(student_object)
        except:
            student_list = []
    else:
        student_objects = Student.objects.all()
        for student_object in student_objects:
            student_list.append(student_object)
    return render(request, 'LandingPage/student_list.html', {'student_list': student_list})
