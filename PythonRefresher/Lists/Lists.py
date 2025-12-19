"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(f"my_list is {my_list}")
my_list.append(1000)
print(f"my_list after appending 1000 is {my_list}")
my_list.insert(2, 1000)
print(f"my_list after inserting 1000 at index 2 is {my_list}")
my_list.remove(8)
print(f"my_list after removing 8 is {my_list}")
my_list.pop(0)
print(f"my_list after popping index 0 is {my_list}")
print(f"my_list[0] is {my_list[0]}")
print(f"my_list[1] is {my_list[1]}")
print(f"my_list[2] is {my_list[2]}")
my_list.sort()
print(f"my_list after sorting {my_list}")

people_list = ["Eric", "Adil", "Jeff"]
print(f"people_list is {people_list}")
print(f"people_list[1] is {people_list[1]}")
print(f"The last element in people_list is {people_list[-1]}")

people_list[0] = "Mel"
print(f"people_list is {people_list}")
print(f"people_list has length {len(people_list)}")
print(f"the first two people from the list are: {people_list[0:2]}")

