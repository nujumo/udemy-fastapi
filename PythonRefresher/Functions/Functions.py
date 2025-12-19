"""
Functions
"""

def my_function():
    print("Inside my_function")

my_function()

def print_my_name(name):
    print(f"Hello {name}!")

print_my_name("Nuala")

def print_my_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

print_my_full_name("Steve", "Jobs")

print("======================")

def print_colour_red():
    colour = "Red" # local variable
    print(colour)

colour = "Blue" # global variable
print(colour)
print_colour_red()

print("======================")
def print_numbers(highest_number, lowest_number):
    print(f"highest_number is {highest_number}")
    print(f"lowest_number is {lowest_number}")

print("print_numbers(10, 3)")
print_numbers(10, 3)
print("print_numbers(3, 10)")
print_numbers(3, 10)
print("print_numbers(lowest_number=3, highest_number=10)")
print_numbers(lowest_number=3, highest_number=10)

print("======================")
def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(10, 6)
print("multiply_numbers(10, 6)")
print(solution)

print("======================")
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [1, 2, 3, 4, 5]
print_list(number_list)

print("======================")
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate

final_cost = buy_item(50)
print("buy_item(50)")
print(f"final_cost is {final_cost}")
