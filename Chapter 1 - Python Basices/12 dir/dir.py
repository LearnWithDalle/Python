# dict = show all thing in class in dictionary format
# help = show all info about only class


class employee:
    def __init__(self, name, salary, age, designation):
        self.name = name
        self.salary = salary
        self.age = 40
        self.designation = designation

a = employee("dalle mahesh", 50000, 25, "maneger")
# print(a.name)
# print(a.__dict__)

# print(help(a))
# print(num.__dir__())










# dir = show all type of method or Function which is apply on specific type of data type we use
str1 = "hello i am string"
print(str1.__dir__())



# # capitalize: Converts the first character to uppercase
print(str1.capitalize())

# # count: Returns the number of occurrences of a substring
# print(str1.count('l'))

# # find: Returns the lowest index of a substring
# print(str1.find('am'))

# # islower: Returns True if all characters in the string are lowercase
# print(str1.islower())

# # upper: Converts all characters to uppercase
# print(str1.upper())

# # replace: Replaces a specified substring with another substring
# print(str1.replace('hello', 'hi'))

# # split: Splits the string into a list based on a specified delimiter
# print(str1.split(' '))

# # strip: Removes leading and trailing whitespaces
# print(str1.strip())

# # isalpha: Returns True if all characters in the string are alphabetic
# print(str1.isalpha())

# # __getitem__: Gets the character at a specific index
# print(str1[2])

# # __add__: Concatenates two strings
# str2 = " and I love Python"
# print(str1 + str2)

# # __contains__: Checks if a substring is present in the string
# print('am' in str1)

# # __mod__: Deprecated, use the format method instead
# print("My name is %s" % "John")

# # __len__: Returns the length of the string
# print(len(str1))
str3 = "hello i am string"
# # __eq__: Checks if two strings are equal
# str3 = "hello i am string"
print(str1 == str3)
