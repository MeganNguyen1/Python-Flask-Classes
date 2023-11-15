myset = {"one", 1, "apple", 1, "apple", True, "one"}
# print(myset)

# print(len(myset))

# print(type(myset))

# newset = set (("hi", 1, 1, 2, 5, 5, "hi"))
# print(newset)

# for i in myset:
#     print(i)

# print(True in myset)

# 1 an True are same for python 
# 0 and False are same for python

# myset.add("Megan")
# print(myset)

myset1 = {2, 4, 5, 7, 7, 2}

# myset.update(myset1)
# print(myset)

# mylist = [1, "red", 0, "hi", 45, "purple"]

# myset.update(mylist)
# print(myset)

# myset.remove(10)
# print(myset)

# raises an error when element is not these in the set

# myset.discard(10)
# print(myset)

# Discard function is also used to delete a particular element anf if the element it not present it doesn't do anything

# myset.pop()
# print(myset)

# Pop function is used to delete  a random element from the set
# set has no order by default, it can stoe the elements in any order

# myset.clear()
# print(myset)

# clear function deletes all the elements if the set

# del myset
# print(myset)

# del keyword deletes the whole set from the program so that you cannot access it further
# if you try to access it there's error

# myset2 = myset.union(myset1)
# print(myset2)

# union function is used to make a new set containing all the elements from both myset and myset1

myset1 = {1, 4, 5, 1, 1, 2, 4, 6, 7}
myset2 = {3, 4, 4, 5, 9, 10, 3}

myset1.intersection_update(myset2)
print(myset1)

# intersection_update function store all the common elements from set1 and set2