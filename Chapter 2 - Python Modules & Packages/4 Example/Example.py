'''
!! PYTHON !! More Example of FUNCTION TUTORIAL 35
EXAMPLE I TOOK IN VIDEO
1. write any function to calculate the area of square
2. write a Python function to multiply all the number in a list
3. whether a number is in a given list
4. create a function show employee in such a way that it should except employee
    name and its salary and display both and if a salary is missing information
    show it as 9000 
5. write a Python function take a number as a parameter and check the number is prime or not
'''

# 1. Solution
# squr = lambda x:x*x
# print(squr(9))

# 2. Solution
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ok(x):
    ans = 1
    for i in x:
        ans = ans * i
    return ans
        
# print(a)
# print(ok(a))

# 3. Solution
# 3. whether a number is in a given list

# def find(x , y):
#     if y in x:
#         print(y,"is in ", x)
#     else:
#         print(y,"is not in ", x)


# find(a , 11)

# 4. Solution
# 4. create a function show employee in such a way that it should except employee
#     name and its salary and display both and if a salary is missing information
#     show it as 9000 

# name = input("Enter Ur name")
# j = 50000

# def shoDetail(x,y=9000):
#     print("Employee Name:", x)
#     print("Employee Salary:", y)
    
    
# shoDetail(name, j)


# ५. solution
# 5. write a Python function take a number as a parameter and check the number is prime or not

# prime : jho number divise ble bye any number expext itself

def check(num):
    if num > 1:
        for i in range(2 , num):
            if(num % i)== 0:
                return 0
            return 1
        
a = int(input("Enter No. chck: "))
ans = check(a)
if ans == 1:
    print(ans, "is prime" )
else:
    print(ans, "is not a prime" )
    