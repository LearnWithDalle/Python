'''types of opretion in List.
list are mutable

1. len: length of the list
2. + : Concatination
3. * : Repetation
4.in : Mebership : the current this "in" the list if yes : true
5. for : Iteration :we can manipulate the list using loop(for)
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ["a", "b", "c", "d", "e"]
c = a + b

print(len(a))
# if len(a) <= 10 :
#     print("run code")
# else:
#     print("fuck U")

# Repetaion
print(a*10)

# membership
print(5 in c)

for x in c:
    print(x)
    
    # !! PYTHON !! Working with LIST UPDATING DELETING TUTORIAL 17