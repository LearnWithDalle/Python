# Updating Dict

ok = {
    'name': "Adity",
    'age': 16,
    'class': 'C',
    'Roll no': 69,
    'email': 'adityagandu@gmail.com'
}
# print(ok)
# ok['age'] = 18
# ok['class']= 'A'
# ok['Roll no']= 5

# print(ok)

# print(ok.keys())
# print(ok.values())

# For only Access a key name
# for x in ok:
#     print(x)

# For Access a key Value


# Delete Dict
'''ok = {
    'name': "Adity",
    'age': 16,
    'class': 'C',
    'Roll no': 69
    'eamil': 'adityagandu@gmail.com'
}'''

# del ok['Roll no']
print(ok)
# del ok
# print(ok)
# ok.clear()

# pop
# ok.pop('email')
# print(ok)

# popitem
ok.popitem()
print(ok)

'''
pop : remove last item
append : add item at last
shipt : add item at first
un-shipt : remove firt item

popitem == js.pop

pop("name")
'''


# property

Namak = {
    1: 10,
    'Quantity': 10000,
    'Company': ['Tata', 'pappu', 'xyz', 'BBk'],   
}
# print(Namak['Company'])
# print(Namak['Company'][1:3])
print(Namak)
# Namak?

# key is naver be a list or Tuple as well