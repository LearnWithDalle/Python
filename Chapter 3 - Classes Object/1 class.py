class emp:
    def __init__(self,Name,Salary,Designation):
        self.name = Name
        self.salary = Salary
        self.designation = Designation
        
dalla = emp("dalle Mahesh",2000000,"onbanch")
# print(dalla.name)
# print(dalla.salary)
# print(dalla.designation)
# print(f"i am {dalla.name}, my salary package is {dalla.salary}, and i work for {dalla.designation}")

'''
class myclass:    
    def method1(self):
        print("this is method one")
    def method2(self, x):
        print("this is method two", x)
def main():
    ok = myclass()
    ok.method1()
    ok.method2(5)
if __name__ == "__main__":
    main()'''
    
class Employee:
    totalEmp = 0
    def __init__(self,name,salary,designation):
        self.name = name 
        self.salary = salary 
        self.designation = designation
        Employee.totalEmp += 1        
        
    def displayEmp(self):
        print(f"Total Employee is : {Employee.totalEmp}")
    def empInfo(self):
        print(f" Employee name: {self.name}\n Salary : {self.salary}\n desination : {self.designation}\n Total Employee: {Employee.totalEmp}")
        
emp1 = Employee("Mukesh", 2000, "Hr")
emp2 = Employee("DALLA", 2000, "ONbANCH")
# emp1.displayEmp()
# emp1.empInfo()
emp2.displayEmp()
# emp2.empInfo()