class Student():
    def __init__(self, firstname, lastname, gpa, major, faculty_advisor):
        self.firstname = firstname
        self.lastname = lastname
        self.gpa = gpa
        self.major = major
        self.faculty_advisor = faculty_advisor

    def get_first(self):
        return self.firstname

    def get_last(self):
        return self.lastname

    def get_gpa(self):
        return self.gpa

    def get_major(self):
        return self.major

    def get_faculty_advisor(self):
        return self.faculty_advisor