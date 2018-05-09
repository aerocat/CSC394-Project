from django.urls import path

from . import views

app_name = 'LandingPage'
urlpatterns = [
	path('', views.index, name='index'),
	path('students/', views.StudentView.as_view(), name='all_students'),
	path('<int:student_id_in>/student', views.StudentSingleView, name='single_student'),
	path('faculty/', views.FacultyView.as_view(), name='all_faculty'),
	path('<int:faculty_id_in>/faculty', views.FacultySingleView, name='single_faculty'),
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('<str:class_code_in>/course', views.CourseSingleView, name='single_course'),
]