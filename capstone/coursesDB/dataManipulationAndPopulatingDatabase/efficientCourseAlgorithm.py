from coursesDB.dataManipulationAndPopulatingDatabase.databaseRetrieval import *

intro_courses = ["CSC400", "CSC401", "CSC402", "CSC403", "CSC406", "CSC407"]
foundation_courses = ["CSC421", "CSC435", "CSC447", "CSC453", "SE450"]
software_systems_electives = ["CSC436", "CSC438", "CSC439", "CSC443", "CSC448", "CSC461", "CSC462", "CSC471",
                              "CSC472", "CSC475", "CSC536", "CSC552", "CSC553", "CSC595", "CNS450", "GAM690",
                              "GAM691", "SE441", "SE452", "SE459", "SE526", "SE554", "SE491", "SE591", "TDC478",
                              "TDC484", "TDC568"]
data_science_electives = ["CSC481", "CSC482", "CSC555", "CSC575", "CSC578", "CSC594"]
database_systems_electives = ["CSC452", "CSC454", "CSC543", "CSC553", "CSC554", "CSC555", "CSC575"]
artificial_intelligence_electives = ["CSC458", "CSC480", "CSC481", "CSC482", "CSC575", "CSC576", "CSC577", "CSC578",
                                     "CSC587", "CSC594"]
software_engineering_electives = ["SE430", "SE433", "SE441", "SE452", "SE456", "SE459", "SE475", "SE477",
                                  "SE480", "SE482", "SE491", "SE554", "SE591"]
game_and_real_time_systems_electives = ["CSC461", "CSC462", "CSC486", "CSC588", "GAM425", "GAM450",
                                        "GAM470", "GAM475", "GAM476", "GAM575", "GAM576", "GAM690",
                                        "GAM691", "SE456"]
human_computer_interactions_electives = ["CSC436", "CSC438", "CSC471", "CSC472", "CSC491",
                                         "HCI440", "HCI430", "HCI454"]

# need to take 4 from any below and then an additional 4 others from any of them
software_systems_classes = 0
theory_classes= 0
data_science_classes = 0
database_systems_classes = 0
artificial_intelligence_classes = 0
software_engineering_classes = 0
game_and_real_time_systems_classes = 0
human_computer_interactions_classes = 0

# what the user wants to take
user_elective_choices = ["CSC436", "CSC438", "CSC595", "CSC448", "CSC462", "SE430", "SE433", "SE452"]

elective_counter = []

courses_completed = set()


def set_user_elective_choices(elective_list):
    global user_elective_choices
    user_elective_choices = elective_list


def make_triple(string_for_first_index, elective_list):
    intersect = set(user_elective_choices).intersection(elective_list)
    return [string_for_first_index, intersect, len(intersect)]


def set_elective_counter():
    elective_counter.append(make_triple("Software Systems Electives", software_systems_electives))
    elective_counter.append(make_triple("Data Science Electives", data_science_electives))
    elective_counter.append(make_triple("Database Systems Electives", database_systems_electives))
    elective_counter.append(make_triple("Artificial Intelligence Electives", artificial_intelligence_electives))
    elective_counter.append(make_triple("Software Engineering Electives", software_engineering_electives))
    elective_counter.append(make_triple("Game and Real Time Systems Electives", game_and_real_time_systems_electives))
    elective_counter.append(make_triple("Human Computer Interaction Electives", human_computer_interactions_electives))


def possible_to_graduate():
    for count in elective_counter:
        if count[2] >= 4:
            return True
    return False


def intros_waived(yesno):
    if yesno:
      for course in intro_courses:
          courses_completed.add(course)


def parse_prereqs(string):
    prereqs = get_prereqs(string)
    prereqs = prereqs.replace("and", " ")
    prereqs = prereqs.replace("or", " ")
    prereqs = prereqs.replace("ConcurrentlyEnrolledin", " ")
    return prereqs.split(" ")

def get_next_quarter(quarter):
    quarters = ["Fall", "Winter", "Spring", "Summer"]
    if quarter == "Summer":
        return "Fall"
    else:
        return quarters[quarters.index(quarter) + 1]


def have_prereqs_for_electives(number, introCourses, current_quarter, classes_per_quarter):
    elective_preference = return_concentration(number)
    have_prereqs_for_electives.courses = []
    have_prereqs_for_electives.done = False
    other_electives = [human_computer_interactions_electives, game_and_real_time_systems_electives,
                       software_engineering_electives, artificial_intelligence_electives,
                      database_systems_electives, data_science_electives, software_systems_electives]
    other_electives.remove(elective_preference)
    have_prereqs_for_electives.elective_counter = 0
    have_prereqs_for_electives.courses_lst = []
    have_prereqs_for_electives.possible_courses = []
    have_prereqs_for_electives.quarter = current_quarter
    if not True != introCourses:
        have_prereqs_for_electives.courses += intro_courses
        have_prereqs_for_electives.possible_courses += elective_preference + foundation_courses
    else:
        have_prereqs_for_electives.possible_courses += elective_preference + intro_courses + foundation_courses
    size = len(elective_preference)
    temp = []
    while not have_prereqs_for_electives.done:
        if len(temp) >= classes_per_quarter:
            temp = []
        if introCourses == False and len(intro_courses) > 0:
            for course in intro_courses:
                prereqs = parse_prereqs(course)
                quarters_offered = get_quarters_offered(course).split(", ")
                if len(temp) < classes_per_quarter:
                    for a in prereqs:
                        if len(temp) < classes_per_quarter and course not in temp:
                            if a == "None":
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)
                            elif a not in have_prereqs_for_electives.courses:
                                if course in temp:
                                    temp.remove(course)
                                break
                            else:
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)
        if (len(temp) < classes_per_quarter):
            for course in foundation_courses:
                prereqs = parse_prereqs(course)
                quarters_offered = get_quarters_offered(course).split(", ")
                if len(temp) < classes_per_quarter:
                    for a in prereqs:
                        if len(temp) < classes_per_quarter and course not in temp:
                            if a == "None":
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)
                            elif a not in have_prereqs_for_electives.courses:
                                if course in temp:
                                    temp.remove(course)
                                break
                            else:
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)
        if (len(temp) < classes_per_quarter) and (size - len(elective_preference) <= 3):
            for course in elective_preference:
                prereqs = parse_prereqs(course)
                if len(temp) < classes_per_quarter:
                    for a in prereqs:
                        if len(temp) < classes_per_quarter and course not in temp:
                            if a == "None":
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)
                            elif a not in have_prereqs_for_electives.courses:
                                if course in temp:
                                    temp.remove(course)
                                break
                            else:
                                if have_prereqs_for_electives.quarter in quarters_offered:
                                    temp.append(course)

        if (len(temp) < classes_per_quarter) and (have_prereqs_for_electives.elective_counter <= 3):
            for course_lst in other_electives:
                for course in course_lst:
                    prereqs = parse_prereqs(course)
                    if len(temp) < classes_per_quarter:
                        for a in prereqs:
                            if len(temp) < classes_per_quarter and course not in temp:
                                if a == "None":
                                    if have_prereqs_for_electives.quarter in quarters_offered and\
                                                    have_prereqs_for_electives.elective_counter < 4:
                                        if(course not in have_prereqs_for_electives.courses):
                                            have_prereqs_for_electives.elective_counter += 1
                                            temp.append(course)
                                elif a not in have_prereqs_for_electives.courses:
                                    if course in temp:
                                        have_prereqs_for_electives.elective_counter -= 1
                                        temp.remove(course)
                                    break
                                else:
                                    if have_prereqs_for_electives.quarter in quarters_offered and \
                                            have_prereqs_for_electives.elective_counter < 4:
                                        if (course not in have_prereqs_for_electives.courses):
                                            have_prereqs_for_electives.elective_counter += 1
                                            temp.append(course)

        if len(temp) >= classes_per_quarter or len(have_prereqs_for_electives.courses) >= 15:
            have_prereqs_for_electives.courses += temp
            have_prereqs_for_electives.courses_lst += [temp]
            for val in temp:
                if val in foundation_courses:
                    foundation_courses.remove(val)
                elif val in elective_preference:
                    elective_preference.remove(val)
                elif val in intro_courses:
                    intro_courses.remove(val)
            have_prereqs_for_electives.quarter = get_next_quarter(have_prereqs_for_electives.quarter)
            if len(have_prereqs_for_electives.courses) >= 19:
                have_prereqs_for_electives.done = True
    return have_prereqs_for_electives.courses_lst


def algorithm(csundergradbool, currenter_quarter):
    intros_waived(csundergradbool)
    set_elective_counter()
    return possible_to_graduate()

def return_concentration(conc_int):
    if(conc_int == 1):
        return software_systems_electives
    elif(conc_int == 2):
        return data_science_electives
    elif(conc_int == 3):
        return database_systems_electives
    elif(conc_int == 4):
        return artificial_intelligence_electives
    elif(conc_int == 5):
        return software_engineering_electives
    elif(conc_int == 6):
        return game_and_real_time_systems_electives
    elif(conc_int == 7):
        return software_engineering_electives



data_science_electives = ["CSC481", "CSC482", "CSC555", "CSC575", "CSC578", "CSC594"]
database_systems_electives = ["CSC452", "CSC454", "CSC543", "CSC553", "CSC554", "CSC555", "CSC575"]
artificial_intelligence_electives = ["CSC458", "CSC480", "CSC481", "CSC482", "CSC575", "CSC576", "CSC577", "CSC578",
                                     "CSC587", "CSC594"]
software_engineering_electives = ["SE430", "SE433", "SE441", "SE452", "SE456", "SE459", "SE475", "SE477",
                                  "SE480", "SE482", "SE491", "SE554", "SE591"]
game_and_real_time_systems_electives = ["CSC461", "CSC462", "CSC486", "CSC588", "GAM425", "GAM450",
                                        "GAM470", "GAM475", "GAM476", "GAM575", "GAM576", "GAM690",
                                        "GAM691", "SE456"]
human_computer_interactions_electives = ["CSC436", "CSC438", "CSC471", "CSC472", "CSC491",
                                         "HCI440", "HCI430", "HCI454"]

print(have_prereqs_for_electives(1, False, "Winter", 4))
