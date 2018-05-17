from coursesDB.objects.courseObject import Course
from coursesDB.objects.courseCatalog import CourseCatalog
from coursesDB.objects.prettyCourseObject import PrettyCourseObject

courseListCatalog = []
courses = []
pretty_courses = []


def file_parser():
    infile = open('../../Q_COURSES2.txt', 'r', encoding='utf-8')
    file_list = infile.readlines()
    infile.close()
    file_list.pop(0)
    for a in file_list:
            courseListCatalog.append(CourseCatalog(a.split("|")))


def make_courses():
    for a in courseListCatalog:
        courses.append(Course(a.courseID, a.courseNumber, a.onlineStatus, a.classSection, a.courseTitle, a.subject,
                              a.subjectDescription, a.classType, a.classTypeDescription, a.consentChar,
                              a.consentDescription,
                              a.enrollmentCap, a.waitListCap, a.enrollStatus, a.classLocation,
                              a.classLocationDescription, a.startTime, a.endTime, a.prereq, a.classNumber,
                              a.classStatus, a.courseDescription))


def construct_pretty_courses():

    infile = open('../../CoursesFileText.txt', 'r', encoding='utf-8')
    file_list = infile.readlines()

    infile = open('../../Q_COURSES2.txt', 'r', encoding='utf-8')
    file_list2 = infile.readlines()

    infile.close()
    file_list.pop(0)
    file_list2.pop(0)

    for a in file_list:
        c = a.split("|")
        count = 0
        isOnline = 'N'
        if(c[8].lower() == 'yes'):
            isOnline = 'Y'
        for b in courses:
            course_string = (b.getSubject()+ str(b.getCourseNumber())).replace(' ', "")
            if c[2] == course_string:
                course_description = b.courseDescription
                if course_description is not None and len(course_description) > 5:
                    pretty_courses.append(PrettyCourseObject(c[2], c[3], c[6], c[9].replace(' ', ""), course_description
                                                         .rstrip('\r\n'), isOnline))
                    count = 1
                    break

        if count == 0:
            for d in file_list2:
                    lst = d.split("|")
                    course_string = str(lst[4] + str(lst[6])).replace(' ', "")
                    if course_string == c[2]:

                        pretty_courses.append(PrettyCourseObject(c[2], c[3], c[6], c[9].replace(' ', ""),
                                                                     lst[16], isOnline))
                        count = 1
                        break
        if count == 0:
            pretty_courses.append(PrettyCourseObject(c[2], c[3], c[6], c[9].replace(' ', ""),
                                                     "CANNOT FIND DESCRIPTION", c[8]))


def get_pretty_courses_list():
    file_parser()
    make_courses()
    construct_pretty_courses()
    return pretty_courses
