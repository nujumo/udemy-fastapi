"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(f"my_set is {my_set}")
print(f"the length of my_set is {len(my_set)}")

for x in my_set:
    print(x)

# print(my_set[0]) # this will throw an error

my_set.discard(3)
print(f"my_set after discarding 3 {my_set}")
my_set.add(6)
print(f"my_set after adding 6 {my_set}")
my_set.update([7,8])
print(f"my_set after updating with 7 and 8 {my_set}")
my_set.clear()
print(f"my_set is {my_set}")

print("=============================")

"""
Tuples are similar to lists but are unordered and cannot be changed
"""
my_tuple = (1, 2, 3, 4, 5)
print(f"my_tuple is {my_tuple}")
print(f"the length of my_tuple is {len(my_tuple)}")
print(f"my_tuple element at index 1 is {my_tuple[1]}")