import json

#This class grabs everything possible about a course. It will be slimmed down in the prettyCourseObject class.

class Course():
    def __init__(self, courseID, courseNumber, onlineStatus, classSection, courseTitle, subject, subjectDescription,
                 classType, classTypeDescription, consentChar, consentDescription, enrollmentCap, waitListCap,
                 enrollStatus,
                 classLocation, classLocationDescription, startTime, endTime, prereq, classNumber, classStatus, courseDescription):
        self.courseID = courseID
        self.courseNumber = courseNumber
        self.onlineStatus = onlineStatus
        self.classSection = classSection
        self.courseTitle = courseTitle
        self.subject = subject
        self.subjectDescription = subjectDescription
        self.classType = classType
        self.classTypeDescription = classTypeDescription
        self.consentChar = consentChar
        self.consentCharDescription = consentDescription
        self.enrollmentCap = enrollmentCap
        self.waitListCap = waitListCap
        self.enrollStatus = enrollStatus
        self.classLocation = classLocation
        self.classLocationDescription = classLocationDescription
        self.startTime = startTime
        self.endTime = endTime
        self.prereq = prereq
        self.classNumber = classNumber
        self.classStatus = classStatus
        self.courseDescription = courseDescription

    def toJson(self):
        courseDictionary =  {"courseID": self.getCourseID(), "courseNumber": self.getCourseNumber(), "onlineStatus":
                self.getOnlineStatus(), "classSection": self.getClassSection(), "courseTitle": self.getCourseTitle,
                "subject": self.getSubject(), "subjectDescription": self.getSubjectDescription(),
                "classType": self.getClassType(), "classTypeDescription": self.getClassTypeDescription(),
                "consentChar": self.getConsentChar(), "consentCharDescription": self.getConsentCharDescription(),
                "enrollmentCap": self.getEnrollmentCap(), "waitListCap": self.getWaitListCap(), "classLocation":
                self.getClassLocation(), "classLocationDescription": self.getClassLocationDescription(),
                "startTime": self.getStartTime(), "endTime": self.getEndTime(), "prereq": self.getPrereq(),
                "classNumber": self.getClassNumber(), "classStatus": self.getClassStatus()}
        return json.dumps(courseDictionary)

    def setCourseID(self, courseID):
        self.courseID = courseID

    def getCourseID(self):
        return self.courseID

    def setCourseNumber(self, courseNumber):
        self.courseNumber = courseNumber

    def getCourseNumber(self):
        return self.courseNumber

    def setOnlineStatus(self, onlineStatus):
        self.onlineStatus = onlineStatus

    def getOnlineStatus(self):
        return self.onlineStatus

    def setClassSection(self, classSection):
        self.classSection = classSection

    def getClassSection(self):
        return self.classSection

    def setCourseTitle(self, courseTitle):
        self.courseTitle = courseTitle

    def getCourseTitle(self):
        return self.courseTitle

    def setSubject(self, subject):
        self.subject = subject

    def getSubject(self):
        return self.subject

    def setSubjectDescription(self, subjectDescription):
        self.subjectDescription = subjectDescription

    def getSubjectDescription(self):
        return self.subjectDescription

    def setClassType(self, classType):
        self.classType = classType

    def getClassType(self):
        return self.classType

    def setClassTypeDescription(self, classTypeDescription):
        self.classTypeDescription = classTypeDescription

    def getClassTypeDescription(self):
        return self.classTypeDescription

    def setConsentChar(self, consentChar):
        self.consentChar = consentChar

    def getConsentChar(self):
        return self.consentChar

    def setConsentCharDescription(self, consentDescription):
        self.consentCharDescription = consentDescription

    def getConsentCharDescription(self):
        return self.consentCharDescription

    def setEnrollmentCap(self, enrollmentCap):
        self.enrollmentCap = enrollmentCap

    def getEnrollmentCap(self):
        return self.enrollmentCap

    def setWaitListCap(self, waitListCap):
        self.waitListCap = waitListCap

    def getWaitListCap(self):
        return self.waitListCap

    def setEnrollStatus(self, enrollStatus):
        self.enrollStatus = enrollStatus

    def getEnrollStatus(self):
        return self.enrollStatus

    def setClassLocation(self, classLocation):
        self.classLocation = classLocation

    def getClassLocation(self):
        return self.classLocation

    def setClassLocationDescription(self, classLocationDescription):
        self.classLocationDescription = classLocationDescription

    def getClassLocationDescription(self):
        return self.classLocationDescription

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getStartTime(self):
        return self.startTime

    def setEndTime(self, endTime):
        self.endTime = endTime

    def getEndTime(self):
        return self.endTime

    def setPrereq(self, prereq):
        self.prereq = prereq

    def getPrereq(self):
        return self.prereq

    def setClassNumber(self, classNumber):
        self.classNumber = classNumber

    def getClassNumber(self):
        return self.classNumber

    def setClassStatus(self, classStatus):
        self.classStatus = classStatus

    def getClassStatus(self):
        return self.classStatus