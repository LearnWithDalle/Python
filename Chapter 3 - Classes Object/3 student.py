class fourth:
    all = 0
    def __init__(self, name, rollNo,):
        self.name = name
        self.rollNo = rollNo
        fourth.all += 1
    def shoInfo(self):
        print(f"name: {self.name}\n Roll No: {self.rollNo}")
    def TotalStu(self):
        print(f"Total Student: {fourth.all}")
        
        
s1 = fourth("adity", 1)
s2 = fourth("adity", 1)
s3 = fourth("adity", 1)
s4 = fourth("adity", 1)
s5 = fourth("adity", 1)
s6 = fourth("adity", 1)
s7 = fourth("adity", 1)

s7.TotalStu()