from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_courses, name='all_courses'),
    path('<course_id>', views.CourseSingleView, name='single_course'),
]
