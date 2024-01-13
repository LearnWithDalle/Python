# What is  Dictionary?
'''
a data we store in our system which is entry or a detail 

dict are also mutable {}
'''
# student data
stu1 = {
    'name': "Adity",
    'age': 16,
    'class': 'D',
    'Roll no': 69
}

emp1 = {
    'name': "shantabai",
    'age': 25,
    'designation': "manager",
    'Emp Id': 69,
    'CTC': 699999
}

print(emp1)  # print
# type()
print(type(emp1))

print(emp1['CTC'])  # Access the value of dict using key

print(emp1.keys())
print(emp1.values())