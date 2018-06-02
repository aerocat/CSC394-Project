from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
# Create your views here.

from accounts.models import Faculty, Student

def index(request):
	return render(request, 'LandingPage/index.html')

class FacultyView(generic.ListView):
	model = Faculty
	context_object_name = 'faculty_list'
	template_name = 'LandingPage/faculty.html'

class StudentView(generic.ListView):
	model = Student
	context_object_name = 'student_list'
	template_name = 'LandingPage/students.html'

def StudentSingleView(request, student_id_in):
	student = Student.objects.get(student_id=student_id_in)

	return HttpResponse("View for student with id %s." % student.student_id)

def FacultySingleView(request, faculty_id_in):
	faculty = Faculty.objects.get(faculty_id=faculty_id_in)

	return HttpResponse("View for faculty with id %s." % faculty.faculty_id)

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
                faculty_list.append(faculty_object)
        except:
            faculty_list = []
    else:
        faculty_objects = Faculty.objects.all()
        for faculty_object in faculty_objects:
            faculty_list.append(faculty_object)
    return render(request, 'LandingPage/faculty_list.html', {'faculty_list': faculty_list})

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
                student_list.append(student_object)
        except:
            student_list = []
    else:
        student_objects = Student.objects.all()
        for student_object in student_objects:
            student_list.append(student_object)
    return render(request, 'LandingPage/student_list.html', {'student_list': student_list})