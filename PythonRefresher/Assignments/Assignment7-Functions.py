"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""
def user_dictionary(firstname, lastname, age):
    new_user_dictionary = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
    }
    return new_user_dictionary

user = user_dictionary(firstname='John', lastname='Doe', age=25)
print(user)