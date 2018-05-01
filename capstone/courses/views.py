from django.shortcuts import render

# Create your views here.
import json

from courses.models import Coursetable
from courses.objects.course import Course
from courses.objects.courseCatalog import CourseCatalog
from django.http import HttpResponse

def index(request):
    #need to change path
    fileParser('/Users/ethancohen/Desktop/untitled/Q_COURSES2.txt')
    makeCourses(courseListCatalog)
    return HttpResponse(getCourse("CSC", 421).getTitle())

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
    for course in courses:
        jCourse = course.toJson
        c = Coursetable(coursec=jCourse, coursesubject=course.getSubject(), coursenumber=course.getCourseNumber())
        c.save()

def getCourse(courseSubject, courseNumber):
    jCourse = Coursetable.objects.get(coursesubject=courseSubject, coursenumber=courseNumber)
    course = json.loads(jCourse)
    return course
