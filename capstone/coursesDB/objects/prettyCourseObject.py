import json


class PrettyCourseObject:

    def __init__(self, course_number, course_name, quarters_offered, prereqs, course_description, offered_online):
        self.course_number = course_number
        self.course_name = course_name
        self.quarters_offered = quarters_offered
        self.prereqs = prereqs
        self.course_description = course_description
        self.offered_online = offered_online

    def to_json(self):
        course_dictionary = {"course_number": self.course_number, "course_name": self.course_name,
                             "quarters_offered": self.quarters_offered, "prereqs": self.prereqs,
                             "course_description": self.course_description, "offered_online": self.offered_online}
        return json.dumps(course_dictionary)
