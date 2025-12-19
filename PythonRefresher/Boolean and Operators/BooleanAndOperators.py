"""
Boolean and Operators
"""

like_coffee = True
like_tea = False

favourite_food = "Pizza"
favourite_number = 32

print(f"Do I like coffee? {like_coffee}")
print(f"Do I like tea? {like_tea}")
print(f"{like_coffee} is type {type(like_coffee)}")
print(f"{like_tea} is type {type(like_tea)}")
print(f"{favourite_food} is type {type(favourite_food)}")
print(f"{favourite_number} is type {type(favourite_number)}")

print("============Comparison Operators================")
print(f"1 == 2 => {1 == 2}")
print(f"1 != 2 => {1 != 2}")
print(f"1 > 2 => {1 > 2}")
print(f"1 < 2 => {1 < 2}")
print(f"1 >= 1 => {1 >= 1}")
print(f"1 <= 2 => {1 <= 2}")

print("============Logical Operators================")
print(f"1 > 3 and 5 < 7 => {1 > 3 and 5 < 7}")
print(f"1 > 3 or 5 < 7 => {1 > 3 or 5 < 7}")
print(f"1 == 1 => {1 == 1}")
print(f"not(1 == 1) => {not(1 == 1)}")