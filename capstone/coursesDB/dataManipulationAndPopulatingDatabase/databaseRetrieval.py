import django
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')
django.setup()


from coursesDB.models import Courses


def get_course(courseNumber):
    jCourse = Courses.objects.get(course_number=courseNumber)
    pretty_course_dict = json.loads(jCourse.course_json)
    return pretty_course_dict


def get_course_number(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["course_number"]


def get_course_name(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["course_name"]


def get_quarters_offered(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["quarters_offered"]


def get_prereqs(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["prereqs"].strip()


def get_course_description(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["course_description"]


def get_offered_online(courseNumber):
    pretty_course_dict = get_course(courseNumber)
    return pretty_course_dict["offered_online"]





'''
{"course_number": self.course_number, "course_name": self.course_name,
                             "quarters_offered": self.quarters_offered, "prereqs": self.prereqs,
                             "course_description": self.course_description, "offered_online": self.offered_online}

print(get_course_number("CSC400"))
print(get_course_name("CSC400"))
print(get_quarters_offered("CSC400"))
print(get_prereqs("CSC400"))
print(get_course_description("CSC400"))
print(get_offered_online("CSC400"))

'''