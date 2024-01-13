# 1. find the factorial of a number
# 5: 5*4*3*2*1: 120
'''user = int(input("Enter the Number: "))

def fact(i):
    ok = 1
    if i < 0:
        print("Negetive Number Not Allow !!")
    elif i == 0:
        print(i)
    elif i == 1:
        print(i)
    else:
        for x in range(1, i + 1):
            ok = ok * x
        print("the Factoriul of", i ,":", ok)
    
fact(user)''' 
        
# 2. write a Python program to reverse the string
# ok = input("Enter Somthing: ")
'''
def revc(x):
    if(len(x) == 0):
        return x
    else:
        return revc(x[1:]) + x[0]
    
if ok == " ":
    print("Bhaiyaa Empty String nahi calegii !!")
else:
    reverse = revc(ok)
    print(reverse)
'''
'''
def rev(x):
    return x[::-1]
revc = rev(ok) 
print(revc)
'''

# 3. program to swap the value of two variables
'''
val1 = "hello dalle"
val2 = "hello Mahesh"

def swap(x,y):
    temp = x
    x = y
    y = temp
    print("Updated old value: ", x)
    print("Updated New value: ", y)

print(" old1 value: ",val1)
print(" old2 value: ",val2)
swap(val1, val2)
'''

# 4. write a Python program which print Fibonacci series of a number til n 
# 0 1 1 2 3 5 8 
'''
ok = int(input("enter the number :"))
n1 = 0
n2 = 1
i = 0
while i < ok:
    print(n1 , end=" , ")
    temp = n1 + n2
    n1 = n2
    n2 = temp 
    i = i + 1
    '''

# 5. write a program which accept an integer value n and display all Odd number till n

'''start = int(input("Enter the starting Number: "))
end = int(input("Enter the Ending Number: "))

for x in range(start , end + 1):
    if x % 2 == 0:
        continue
    else:
        print(x)'''
        
# 6. write a program to reverse given number
'''num = int(input("Enter the Number: "))
sum = 0
while (num != 0):
    d = num % 10
    sum = (sum * 10) + d
    num = num // 10
    
print(sum)
   '''

# 7. write a program to display the following patter
'''
*****
 ****
  ***
   **
    *
'''

star = int(input("Enter the No: "))

for x in range(star, 0, -1):
    print((star - 1) * " " + x * " * ")
    
    !! PYTHON !! FUNCTION : Examples With Solution Part 2 TUTORIAL 26
    


