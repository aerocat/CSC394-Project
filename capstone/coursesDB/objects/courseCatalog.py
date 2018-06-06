from django.conf import settings


class CourseCatalog():
    # Initializes course variables based on column in excel sheet
    def __init__(self, courseList):

        # Int that is course ID if courseID needs to have leading 0's, store as a string
        self.courseID = int(courseList[0])

        # Int that is course number, EX: our class is CSC 394, so it would be 394
        self.courseNumber = int(courseList[6])

        # Boolean that is True if online, false if in class section, none if error
        self.onlineStatus = self.isOnline(courseList[2])

        # Int that all begin with 9 so i am not sure if this is what correlates with quarter taught
        self.classSection = int(courseList[7])

        # String that is the course title example: Software Projects
        self.courseTitle = courseList[15]

        # String that is CSC, IS, HCI, IS, SE, or ECT
        self.subject = courseList[4]
        # String that is the subject, unabbreviated
        self.subjectDescription = courseList[5]

        # String that is either LEC or IND
        self.classType = courseList[9]
        # String that is the classType, unabbreviated
        self.classTypeDescription = courseList[10]

        # String for type of consent needed, can be I, D, or N
        self.consentChar = courseList[17]
        # String that if the consentChar, unabbreviated
        self.consentDescription = courseList[18]

        # Integer for enrollment cap for each class
        self.enrollmentCap = int(courseList[21])
        # Integer for wait list cap
        self.waitListCap = int(courseList[22])
        # String for enroll status, can be C or O. Assuming this is closed or open
        # so i do not know why some would be closed.
        self.enrollStatus = courseList[20]

        # String for class location
        self.classLocation = courseList[23]
        # String for the Decripstion of the class location
        self.classLocationDescription = courseList[24]

        # String Time for start time for class(stored in HH:MM)
        self.startTime = self.getTime(courseList[31])

        # String,  Time for end time for class(stored in HH:MM)
        self.endTime = self.getTime(courseList[32])

        # String Determines whetrher a class has a prereq. The string Starts with either the prereq courses or is None
        self.prereq = self.prereqStringSolver()
        # BELOW THIS AREA ARE VARIABLE THAT I DO NOT BELIEVE ARE NECESSARY
        # I did not include the following columns since there is no variation
        # COLUMN B, COLUMN N, COLUMN O, COLUMN Z, COLUMN AA, COLUMN AB, COLUMB AC
        # COLUMB AD, COLUMN AE

        # Int that is the class number associated with the class
        self.classNumber = int(courseList[8])

        # String for class status, can be A, T, or X
        self.classStatus = courseList[19]

        self.courseDescription = self.prereqFinder()

    # Helper method to pair courses from one excel sheet  to the other since the prerequistes are cut off in one
    # document
    def prereqFinder(self):
        # THIS PATH WILL CHANGE WITH EACH USER
<<<<<<< HEAD
        infile = open('../../Q_COURSES-1.txt', 'r', encoding='utf-8')
=======
        infile = open(settings.PATH_COURSE1, 'r', encoding='utf-8')
>>>>>>> master
        fileList = infile.readlines()
        fileList.pop(0)
        for a in fileList:
            a = a.split("|")
            if (self.subject + str(self.courseNumber) == (a[2] + a[3]).strip()):
                return a[19]
        return None

    # Helper method that splits string at prerequisite in the discription and
    # then formats it to only have courses and preqreq descriptions
    def prereqStringSolver(self):
        st = self.prereqFinder()
        if (st != None):
            st = st.strip()
            st = st.upper()
            stList = st.split("PREREQUISITE")
            if (len(stList) > 1):
                return stList[1].strip("(S):").strip(":").lstrip()
        return None

    # helper method for checking if a course is online
    def isOnline(self, sessionCode):
        if (sessionCode == "1"):
            return False
        elif (sessionCode == "OLS"):
            return True
        else:
            return None

    def getTime(self, timeString):
        if (len(timeString) == 1):
            return "00:00"
        elif (len(timeString) == 3):
            return "0" + timeString[0] + ":" + timeString[1:]
        return timeString[0:2] + ":" + timeString[2:]
