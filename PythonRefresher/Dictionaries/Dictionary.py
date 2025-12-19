"""
Dictionaries
"""

user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

print(f"user_dictionary => {user_dictionary}")
print(f"user_dictionary['username'] => {user_dictionary['username']}")
print(f"user_dictionary.get('username') => {user_dictionary.get('username')}")
user_dictionary["married"] = True
print(f"user_dictionary after adding 'married' key => {user_dictionary}")
print(f"user_dictionary has length => {len(user_dictionary)}")
user_dictionary.pop("age")
print(f"user_dictionary after removing 'age' key => {user_dictionary}")

for x in user_dictionary:
    print(x)

for x , y in user_dictionary.items():
    print(x, y)


user_dictionary2 = user_dictionary.copy() # use copy() to clone the dictionary
user_dictionary2.pop("married")
print(f"user_dictionary => {user_dictionary}")
print(f"user_dictionary2 => {user_dictionary2}")

user_dictionary.clear()
print(f"user_dictionary after clearing => {user_dictionary}")

del user_dictionary