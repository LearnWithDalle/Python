# 2. Multiple Inheritance
# Basic Example

class Student:
    def getData(self,  name, rollno, course):
        self.name = name
        self.rollno = rollno
        self.course = course

    def displayStudent(self):
        print("name:", self.name)
        print("Roll Number:", self.rollno)
        print("Course:", self.course)
# Inheritance.


class Test (Student):
    def getMarks(self, marks):
        self.marks = marks

    def displayMarks(self):
        print("Total Marks:", self.marks)


class Sports:
    def getSportsMarks(self, spmarks):
        self.spmarks = spmarks

    def displaySportsMarks(self):
        print("Sports Marks:", self.spmarks)
# Multiple Inheritance


class Result(Test, Sports):
    def calculateGrade(self):
        m = self.marks + self.spmarks
        if m > 80:
            self.grade = "excellent"
        elif m > 60:
            self.grade = "Good"
        elif m >40:
            self.grade = "Bad"
        else:
            self.grade = "Failed"
        print(f"result : {self.grade}")

# Start


r = int(input("Enter Ur Roll No: "))
n = input("Enter Ur name: ")
c = input("Enter Ur Course: ")
m = int(input("Enter Marks: "))
s = int(input("Enter Sports Marks: "))

s1 = Result()
s1.getData(n, r, c)
s1.getMarks(m)
s1.getSportsMarks(s)
s1.displayStudent()
s1.displayMarks()
s1.displaySportsMarks()
s1.calculateGrade()
