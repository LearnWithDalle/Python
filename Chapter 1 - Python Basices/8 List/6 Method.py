'''
Python includes following list methods:

1. list.append(obj): Appends object obj to list.
2. list.count(obj): Returns count of how many times obj occurs in list.
3. list.extend(seq): Appends the contents of seq to list.
4. list.index(obj): Returns the lowest index in list that obj appears.
5. list.insert(index, obj): Inserts object obj into list at offset index.
6. list.pop(obj=list[-1]): Removes and returns last object or obj from lit.
7. list.remove(obj): Removes object obj from list.
8. list.reverse(): Reverses objects of list in place.
9. list.sort([func]): Sorts objects of list, use compare func if given.
10.clear(): Removes all items from the list.
11.copy(): Returns a shallow copy of the list
'''

# Example
l = [1, 2, 3, 2, 4, 5]
print("old List : ", l)
# 1. list.append(obj)
# l.append(6)
# print("append:", l)  # Output: [1, 2, 3, 2, 4, 5, 6]

# # 2. list.count(obj)
# ok = l.count(2)
# print("count:", ok)  # Output: 2

# 3. list.extend(seq)
# l.extend([7, 8])
# print("extend:", l)  # Output: [1, 2, 3, 2, 4, 5, 6, 7, 8]

# 4. list.index(obj)
# ok = l.index(4)
# print("index:", ok)  # Output: 4

# 5. list.insert(index, obj)
# l.insert(2, 9)
# print("insert:", l)  # Output: [1, 2, 9, 3, 2, 4, 5, 6, 7, 8]

# 6. list.pop(obj=list[-1])
# ok = l.pop()
# print("pop:", ok, l)  # Output: 8 [1, 2, 9, 3, 2, 4, 5, 6, 7]

# 7. list.remove(obj)
# l.remove(2)
# print("remove:", l)  # Output: [1, 9, 3, 2, 4, 5, 6, 7]

# # 8. list.reverse()
# l.reverse()
# print("reverse:", l)  # Output: [7, 6, 5, 4, 2, 3, 9, 1]

# 9. list.sort([func])
# l.sort()
# print("sort:", l)  # Output: [1, 2, 3, 4, 5, 6, 7, 9]

# 10. clear()
# l.clear()
# print("clear:", l)  # Output: []

# 11. copy()
# ok = [1, 2, 3]
# le = ok.copy()
# print("copy:", le)  # Output: [1, 2, 3]


# !! PYTHON !! LIST ALL FUNCTION OR METHODS TUTORIAL 18