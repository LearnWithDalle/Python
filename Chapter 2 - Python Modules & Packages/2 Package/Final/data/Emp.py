class Emp:
    def __init__(self, employee):
        self.name = employee['name']
        self.Designation = employee['Designation']
        self.gender = employee['Gender']
    def get_employee_details(self):
        return (f"Name: {self.name}\nDesignation: {self.Designation}\nGender : {self.gender}")