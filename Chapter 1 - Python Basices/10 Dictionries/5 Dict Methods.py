'''
Python includes following dictionary methods:
1. dict.clear(): Removes all elements of dictionary dict.
2. dict.copy(): Returns a shallow copy of dictionary dict.
3. dict.fromkeys(): Create a new dictionary with keys from seq and values set to value.
4. dict.get(key, default=None): For key key, returns value or default if key not in dictionary.
5. dict.has_key(key): Returns true if key in dictionary dict, false otherwise.
6. dict.items(): Returns a list of dict's (key, value) tuple pairs.
7. dict.keys(): Returns list of dictionary dict's keys.
8. dict.setdefault(key, default=None): Similar to get(), but will set dict[key]=default if key is not already in dict.
9. dict.update(dict2): Adds dictionary dict2's key-values pairs to dict.
10. dict.values(): Returns list of dictionary dict's values.
'''

# # Example dictionary
ok = {'a': 1, 'b': 2, 'c': 3}
print(ok)

# 1. dict.clear(): Removes all elements of dictionary dict.
# # 1. dict.clear()
# ok.clear()
# print("clear:", ok)  # Output: {}

# 2. dict.copy(): Returns a shallow copy of dictionary dict.
# # 2. dict.copy()
# copy = ok.copy()
# print("copy:", copy)  # Output: {}

# 3. dict.fromkeys(): Create a new dictionary with keys from seq and values set to value.
# 3. dict.fromkeys(seq, value)
# le = dict.fromkeys(['x', 'y', 'z'], 0)
# print("fromkeys:", le)  # Output: {'x': 0, 'y': 0, 'z': 0}

# 4. dict.get(key, default=None): For key key, returns value or default if key not in dictionary.
# # 4. dict.get(key, default=None)
# value = ok.get('z', 'Fuck U')
# print("get:", value)  # Output: Not Found

# 5. dict.has_key(key): Returns true if key in dictionary dict, false otherwise.
# # 5. key in dict (alternative to has_key)
# exist = 'a' in ok
# print("Key in Dict:", exist)  # Output: False

# 6. dict.items(): Returns a list of dict's (key, value) tuple pairs.
# 6. dict.items()
items = ok.items()
print("items:", items)  # Output: dict_items([])
# ([(1,2),(3,1),(2,3),(1,2),(3,1),(2,3)])

# 7. dict.keys(): Returns list of dictionary dict's keys.
# # 7. dict.keys()
# keys = ok.keys()
# print("keys:", keys)  # Output: dict_keys([])

# 8. dict.setdefault(key, default=None): Similar to get(), but will set dict[key]=default if key is not already in dict.
# 8. dict.setdefault(key, default=None)
# ok.setdefault('a', 0)
# ok.setdefault('x', 10)
# print("setdefault:", ok)  # Output: {'a': 0, 'x': 10}
# It work when key value is invalid or not set

# 9. dict.update(dict2): Adds dictionary dict2's key-values pairs to dict.
# 9. dict.update(dict2)
# le = {'b': 20, 'y': 30}
# ok.update(le)
# print("update:", ok)  # Output: {'a': 0, 'x': 10, 'b': 20, 'y': 30}

# 10. dict.values(): Returns list of dictionary dict's values.
# 10. dict.values()
# values = ok.values()
# print("values:", values)  # Output: dict_values([1, 2, 3])



