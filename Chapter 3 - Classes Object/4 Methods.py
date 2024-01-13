'''
1. Instance Method
2. Static Method
3. Class Method
'''
    
'''string = "python"
def text(string):
    string = "i love Coding"
    print(f"inside of code: {string}")
    
text(string)
print(f"OutSide of code: {string}")'''
        
        
        
# 1. Instance Method
 
 
class fourth:
    all = 0
    ok = "bhai tu Awsome Hai"
    def __init__(self, name, rollNo): #instance Methode
        self.name = name
        self.rollNo = rollNo
        fourth.all += 1
    def shoInfo(self):
        print(f" name: {self.name}\n Roll No: {self.rollNo}")
    def TotalStu(self):
        print(f"Total Student: {fourth.all}")
    @staticmethod
    def greeting(): # this is Static Method
        print("Thanks for Using This class")
    @classmethod
    def classwalamethode(clme):
        print(f"this is class methode: {clme.ok}")        

        
    
        

s1 = fourth("Riya", 26)
s1.shoInfo()
s1.classwalamethode()