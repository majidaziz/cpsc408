import sqlite3
from Student import Student


class Rover:
    conn = sqlite3.connect('StudentDB.sqlite')
    c = conn.cursor()

    def display_all(self):
        # obtains everything from Student table
        self.c.execute("SELECT * FROM Student")
        data = (self.c.fetchall())
        # outputs to console new line each row
        print()
        print("[StudentID | FirstName | LastName | GPA |  Major | Faculty Advisor]")
        print()
        for row in data:
            print(row)

    # obtains data to create and add student to database
    def create_student(self):
        print()
        print("--CREATE STUDENT--")
        print()
        while True:
            try:
                firstname = input("first name: ")
                lastname = input("last name: ")
                gpa = float(input("gpa: "))
                major = input("major: ")
                faculty_advisor = input("faculty_advisor: ")
                stu = Student(firstname, lastname, gpa, major, faculty_advisor)
                self.c.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdvisor) VALUES (?, ?, ?, ?, ?)",
                          (stu.get_first(), stu.get_last(), stu.get_gpa(), stu.get_major(), stu.get_faculty_advisor()))
                print("--student created successfully--")
                break;
            except ValueError:
                print("Incorrect input, try again")
            # inserts into table(should autoincrement...i think)

    def update(self):
        print()
        print("--UPDATE STUDENT--")
        print()
        eyeD = int(input("type '0' to list students: "))
        # displays table tuples
        if eyeD == 0:
            self.display_all()
            print()
            eyeD = int(input("ENTER STUDENT_ID: "))
        # I've noticed certain formats produce errors for certain statements
        sql_cmd = "SELECT FirstName FROM Student WHERE StudentID = '{}'".format(eyeD)
        self.c.execute(sql_cmd)
        # person = the previous input int from console and retrieve student id from db
        # then prints name of student id asking to update which attribute
        person = self.c.fetchall()
        choice = int(input("UPDATE " + str(person) + "; MAJOR(1), ADVISOR(2), NEITHER(3): "))
        # executes option given user input
        if choice == 1:
            val = input("SET MAJOR: ")
            self.c.execute("UPDATE Student SET Major = ? WHERE StudentID = ?", (val, eyeD))
        elif choice == 2:
            val = input("SET ADVISOR: ")
            self.c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentID = ?", (val, eyeD))

    # easy: deletes tuple from table given StudentID by user input via console
    def delete(self):
        print()
        eyeD = int(input("Delete student by StudentID: "))
        self.c.execute("DELETE FROM Student WHERE StudentID = '{}'".format(eyeD))
        print("successfully deleted")

    # search function capable of 3 different search key words: major, gpa, advisor.
    def search(self):
        print()
        print("--SEARCH TABLE--")
        print()
        choice = int(input("Search by MAJOR(1) GPA(2) or ADVISOR(3): "))
        if choice == 1:
            field = input("ENTER MAJOR: ")
            self.c.execute("SELECT * FROM Student WHERE Major = '{}'".format(field))
            data = self.c.fetchall()
            # outputs to console new line each row
            print("[StudentID | FirstName | LastName | GPA |  Major | Faculty Advisor]")
            for row in data:
                print(row)
        elif choice == 2:
            field = float(input("ENTER GPA: "))
            self.c.execute("SELECT * FROM Student WHERE GPA = '{}'".format(field))
            data = self.c.fetchall()
            # outputs to console new line each row
            print("[StudentID | FirstName | LastName | GPA |  Major | Faculty Advisor]")
            for row in data:
                print(row)
        elif choice == 3:
            field = input("ENTER ADVISOR: ")
            self.c.execute("SELECT * FROM Student WHERE FacultyAdvisor = '{}'".format(field))
            data = self.c.fetchall()
            # outputs to console new line each row
            print("[StudentID | FirstName | LastName | GPA |  Major | Faculty Advisor]")
            for row in data:
                print(row)

    # Creates a table named Student if it doesn't already exist.
    def create_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS Student (
        StudentId INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName VARCHAR(25),
        LastName VARCHAR(25),
        GPA real,
        Major VARCHAR(10),
        FacultyAdvisor VARCHAR(25)
        )""")

    # helper helping helpess methods
    @staticmethod
    def helper():
        print("Create Student(1) | Display All(2) | Update(3) | Delete(4) | Search(5) | Exit(6)")

    def explore(self):
        # start program by setting table
        self.create_table()
        print("Table connected succesfully")
        print("Type '0' to LIST COMMANDS")
        # this while contains the continuous segment of the program, if false program ends.
        while True:
            cmd = int(input("main-operation: "))
            if cmd == 0:
                self.helper()
            elif cmd == 1:
                self.create_student()
            elif cmd == 2:
                self.display_all()
            elif cmd == 3:
                self.update()
            elif cmd == 4:
                self.delete()
            elif cmd == 5:
                self.search()
            elif cmd == 6:
                # must exit in order to save changes to db
                print("My battery is low and it's getting dark.")
                self.conn.commit()
                self.conn.close()
                break

