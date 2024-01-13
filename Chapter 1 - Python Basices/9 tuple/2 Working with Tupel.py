'''
TUPLE IS IMUTABLE
'''

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)

# 1. concatimnation
t3 = t1 + t2
# print(t3)

# DELETE TUPEL
# del t2

print(t3)


# Write a python Program to delete the element from the tuple

# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
ok = t3[:3] + t3[7:]
print(ok)