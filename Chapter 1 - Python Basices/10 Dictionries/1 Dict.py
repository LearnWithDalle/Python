# What is  Dictionary?
'''
a data we store in our system which is entry or a detail 

dict are also mutable {} but
key is imutable
and the value is Mutable
'''
# student data
stu1 = {
    'name': "Adity",
    'age': 16,
    'class': 'C',
    'Roll no': 69
}

emp1 = {
    'name': "Shantaram",
    'age': 25,
    'designation': "Chaprasi",
    'Emp Id': 69,
    'CTC': 6969
}

print(emp1)  # print
# type()
# print(type(emp1))

# print(emp1['CTC'])  # Access the value of dict using key

# print(emp1.keys())
# print(emp1.values())

ok = "Dallle tu best hai bhai"
print(ok)
ok = list(ok)
print(ok)

'''
Dict Sintax

Sintax 1
DictName = {
    DictKey : DictValue,
    DictKey : DictValue,
    DictKey : DictValue,
    .
    .
    DictKey : DictValue
}


Sintax 2
DictName = dict([
    (DictKey , DictValue),
    (DictKey , DictValue),
    (DictKey , DictValue),
    .
    .
    (DictKey , DictValue)
])

'''
l = dict([
    (1, 2),
    (3, 5),
    (65, 6),
    (9, 5),
    (696, 63)
])
print(l)
print(type(l))