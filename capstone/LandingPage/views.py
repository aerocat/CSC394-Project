from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
# Create your views here.

from .models import Faculty, Student

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