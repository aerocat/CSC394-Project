from django.contrib import admin
from django.urls import path, include
from course_search import views

app_name = 'course_search'
urlpatterns = [
    path('', views.courseSearch, name='course-search'),
]