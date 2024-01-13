# 1. Single Inheritance

'''class animal:
    def eat():
        print("Eating..........")
class Dog(animal):
    def bark():
        print("Barking...... Bhau Bhau ")

d = Dog
d.eat()
d.bark()
'''


class Student:
    def data(self, name, rollNo,  course):
        self.name = name
        self.rollNo = rollNo
        self.course = course
    def show(self):
        print(f" name: {self.name}\n roll No: {self.rollNo}\n cource: {self.course}")

# real
class test(Student):
    def getmark(self, mark):
        self.mark = mark
    def showMark(self):
        print(f" marks: {self.mark}")
                
name = "Darshan"
rollNo = 20
course = "Java"
mark = 40


s1 = test()
s1.data(name,rollNo,course)
s1.getmark(mark)
s1.show()
s1.showMark()

'''
OutPut:
 name: Darshan
 roll No: 20
 cource: Java
 marks: 40
'''