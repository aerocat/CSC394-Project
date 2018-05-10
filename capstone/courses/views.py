from django.shortcuts import render

# Create your views here.
import json
from courses.models import Coursetable
from courses.objects.course import Course
from courses.objects.courseCatalog import CourseCatalog
from django.http import HttpResponse

def index(request):
    #need to change path
    fileParser('/Users/ethancohen/Documents/CSC394-Project/capstone/Q_COURSES2.txt')
    makeCourses(courseListCatalog)
    jCourse = Coursetable.objects.get(pk=5)
    course = json.loads(jCourse)
    return HttpResponse({'course': course}, content_type='application/json')

courseListCatalog = []
courses = []

def fileParser(fileName1):
    infile = open(fileName1, 'r', encoding='utf-8')
    fileList = infile.readlines()
    infile.close()
    fileList.pop(0)
    for a in fileList:
            courseListCatalog.append(CourseCatalog(a.split("|")))


def makeCourses(courseList):
    for a in courseList:
        courses.append(Course(a.courseID, a.courseNumber, a.onlineStatus, a.classSection, a.courseTitle, a.subject,
                              a.subjectDescription, a.classType, a.classTypeDescription, a.consentChar,
                              a.consentDescription,
                              a.enrollmentCap, a.waitListCap, a.enrollStatus, a.classLocation,
                              a.classLocationDescription, a.startTime, a.endTime, a.prereq, a.classNumber,
                              a.classStatus))
    for course in courses[:10]:
        jCourse = course.toJson()
        print(json.loads(jCourse))
        c = Coursetable(coursec=jCourse, coursesubject=course.getSubject(), coursenumber=course.getCourseNumber())
        c.save()

def getCourse(courseSubject, courseNumber):
    jCourse = Coursetable.objects.get(coursesubject=courseSubject, coursenumber=courseNumber)
    course = json.loads(jCourse)
    return course
