class Student:
    #studentname=""

    def __init__(self, name, major, gpa, is_on_probation):
        self.studentname = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation



    def on_honor_roll(self):
        if self.gpa > 4.0:
            return True
        else:
            return False
