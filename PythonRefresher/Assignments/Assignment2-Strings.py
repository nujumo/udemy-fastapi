"""
String Assignment

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed...
"""

days = int(input("How many days until your birthday? "))
num_days_in_week = 7
# print(type(days))
print(f"There are {days / num_days_in_week} weeks until your birthday!")
print(f"There are {round(days / num_days_in_week, 2)} weeks until your birthday!")