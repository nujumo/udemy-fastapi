"""
For and While Loops
"""

my_list = [1, 2, 3, 4, 5]
print(f"my_list is {my_list}")
print(f"my_list[0] is {my_list[0]}")
print(f"my_list[1] is {my_list[1]}")
print(f"my_list[2] is {my_list[2]}")
print(f"my_list[3] is {my_list[3]}")
print(f"my_list[4] is {my_list[4]}")

for iterator in my_list:
    print(iterator)

sum_of_for_loop = 0
for x in my_list:
    sum_of_for_loop += x
print(f"sum_of_for_loop is {sum_of_for_loop}")

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for x in my_list:
    print(f"Happy {x}!")

print("========WHILE LOOP============")
i = 0
while i < 5:
    i += 1
    print(i)

print("========")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("========")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i is now larger or equal to 5")

print("========")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i==4:
        break
else:
    print("i is now larger or equal to 5")