from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_courses, name='all_courses'),
]
