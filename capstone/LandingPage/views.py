from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
# Create your views here.

from .models import Faculty, Student
from course_search.models import Course

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

class CourseListView(generic.ListView):
	model = Course
	context_object_name = 'course_list'
	template_name = 'LandingPage/course_list.html'
	
def CourseSingleView(request, class_code_in):
	course = Course.objects.get(class_code=class_code_in)

	return HttpResponse("View for course with class code %s." % course.class_code)