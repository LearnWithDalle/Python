# 1. Write a Python Code to add key to a Dict
# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}

# print(a)
# a.update(b)
# print(a)
# a.update(c)
# print(a)
e = {}
for d in (a, b, c):
    e.update(d)

# print(e)


# 2. Write a Python Code to Check if Key is Exis or not
# print(e)

# if 10 in e:
#     print("Yes bro 5 is in  e: ", e)
# else:
#     print("nahi hai e ke under: ", e)


# 3. Write a Python Code to print the Dict in this Format
# Key => Value

# print(e)

# for ok, le in e.items():
#     print(ok, "=>", le)


# 4. Write a Python Code to Generate the Square No.
# till User's No.
# Example : user n = 2, OutPut: {1:1, 2:4}.

dalle = int(input("Enter the Fucking No: "))
a = dict()
print(a)

for x in range(1, dalle + 1):
    a[x] = x*x
    
print(a)

