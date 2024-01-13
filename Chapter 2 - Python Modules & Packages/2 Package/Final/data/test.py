from Student import Student
from Emp import Emp

student1 = {
    "name": "Dalle",
    "gender": "Unknown",
    "age": 19
}
ok = {
    "name": "Gadhha",
    "Designation":"Fullstack",
    "Gender": "TransGender"
}

student = Student(student1)
employee = Emp(ok)


print(student.get_student_details())
print(employee.get_employee_details())
