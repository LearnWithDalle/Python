'''
class Employee:
    def __init__(self, name,age):
        self.name = name 
        self.age = age
    def showEmp(self):
        print(f"Name of Employee: {self.name}\n age of Employee: {self.age}")

class data:
    def __init__(self, address, salary ,empInfo):
        self.address = address
        self.salary = salary
        self.empInfo = empInfo
    def displayData(self):
        self.empInfo.showEmp()
        print(f"Address of Employee: {self.address}\n salary of Employee: {self.salary}\n")
        

emp1 = Employee("PappuChaiWala", 69)
data1 = data("Mumbai", 69000, emp1)
data1.displayData()
'''

'''
Example 2 :
    Python program to create a class in which one method accept the string from the user and another method printed define a class name country which has a method called print nationality define subclass name state from country which has a method called print state write the method to print state country and nationality.
'''

'''
class accept:
    def userstr(self):
        self.a = input("Enter the String : ")

    def showstr(self):
        print(f"string is : {self.a}")


a = accept()
a.userstr()
a.showstr()


class Country:
    def getNash(self):
        self.country = input("Enter the Country name: ")
        self.Nashnality = input("Enter your Nashnality: ")

    def nash(self):
        print(f"Country is : {self.country}")
        print(f"Nashnality is : {self.Nashnality}")


class State(Country):
    def getsta(self):
        self.state = input("Enter your State: ")

    def shaowState(self, ok):
        ok = ok
        print(f"State is : {self.state}")


st = State()
st.getNash()
st.getsta()
st.shaowState(st.nash())
'''

'''
Example 3
create a python class which first method input the string from the User second method print that string into UpperCase after that print that string in reverse word by word

Example 4
Python program to accept delete in this place student details such as roll number name marks in three subject using classes also display percentage of each student
'''


# create a python class which first method input the string from the User second method print that string into UpperCase after that print that string in reverse word by word


'''class str:
    def str1(self):
        self.string = input("Enter the String: ")
    def printstr(self):
        print(f"Normal string: {self.string}")
        print(f"UpperCase string: {self.string.upper()}")
        print(f"Revese Mode : {self.string[::-1]}")

a = str()
a.str1()
a.printstr()'''

# Python program to accept, delete and display student details such as roll number, name, marks in three subject using classes also display percentage of each student


class student:
    def accept(self):
        self.name = input("Enter Ur name: ")
        self.RollNo = int(input("Enter Ur Roll No: "))
        self.marks = list()
        for i in range(0, 3):
            self.ok = int(input(f"Enter {i} subject marks: "))
            self.marks.append(self.ok)

    def display(self):
        print(f"Name : {self.name}\nRoll No: {
              self.RollNo}\nMarks : {self.marks}")
        print(f"percentage: {sum(self.marks) * 100 / 300}%")


total = int(input("Total Number Of Student: "))
stu = []
for i in range(0, total):
    ok = input(f"Enter {i} Student name:")
    stu.append(ok)
print(stu)

for j in range(len(stu)):
    stu[j] = student()
    stu[j].accept()
    stu[j].display()
