'''
class : Bunch of code
obj = class 
Dict:
    dalla = {
        "name": "dalla",
        "age": 69,
        "Gender": "Unknown",    
        }
'''


class person:
    all = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        person.all += 1       
    def Showinfo(self):
        print(f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}")
    def totalPerson(self):        
        print(f"Total person: {person.all}")
    def method3():
        print("hello this is method 3")

p1 = person("Dalla" , 25, "Unknown")
p1.method3()

p2 = person("Priya", 20, "female")
p3 = person("Priya", 20, "female")

# p1.Showinfo()
# p2.Showinfo()

p2.totalPerson()

