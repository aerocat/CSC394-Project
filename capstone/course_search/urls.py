from django.contrib import admin
from django.urls import path, include
from courses import views

from course_search.views import CourseListView
from course_search.views import CourseSingleView

app_name = 'course_search'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CourseListView.as_view(), name='course-list'),
    path('<str:class_code_in>/course_search', CourseSingleView, name='single_course'),
]