import django
import os
import sys
sys.path.insert(0, "/Users/Marco/Documents/Senior_Year/Capstone/capstone")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')
django.setup()

from coursesDB.models import Courses
from coursesDB.dataManipulationAndPopulatingDatabase.createCoursesObjects import get_pretty_courses_list

django.setup()

Courses.objects.all().delete()


pretty_courses = get_pretty_courses_list()
print(len(pretty_courses))
for course in pretty_courses:
    jCourse = course.to_json()
    c = Courses(course_json=jCourse, course_number=course.course_number)
    c.save()
