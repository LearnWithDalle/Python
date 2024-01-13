'''
Python includes the following list functions:

1. all(): Return True if all elements of the list are true (or if the list is empty).

2. any(): Return True if any element of the list is true. If the list is empty, 
return False.

3. enumerate(): Return an enumerate object. It contains the index and value
of all the items of list as a tuple.

4. len(): Return the length (the number of items) in the list.

5. list(): Convert an iterable (tuple, string, set, dictionary) to a list.

6. max(): Return the largest item in the list.

7. min(): Return the smallest item in the list.

8. sorted(): Return a new sorted list (does not sort the list itself).

9. sum(): Return the sum of all elements in the list.
'''
# Example
l = [True, False, True, True, False]
# l = [1,32,54,1,1,2,98,269,1,5]
# l = [True, True , True, True, True]

# 1. all()
# ok = all(l)
# print("l is  True or False:", ok)  # Output: False

# 2. any()
# ok = any(l)
# print("any():", ok)  # Output: True

# 3. enumerate()
# ok = list(enumerate(l))
# print("enumerate():", ok)  # Output: [(0, True), (1, False), (2, True), (3, True), (4, False)]

# 4. len()
# ok = len(l)
# print("len():", ok)  # Output: 5

# 5. list()
# le = "hello Mahesh Dalle"
# ok = list(le)
# print("list():", ok)  # Output: [1, 2, 3]

# # 6. max()
# ok = max(l)
# print("max():", ok)  # Output: True

# # 7. min()
# ok = min(l)
# print("min():", ok)  # Output: False

# # 8. sorted()
# ok = sorted(l)
# print("sorted():", ok)  # Output: [False, False, True, True, True]

# 9. sum()
le = [1,2,3,4,5,6,7,8,9]
ok = sum(le)
print("sum():", ok)  # Output: 45

