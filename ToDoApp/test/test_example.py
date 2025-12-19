import pytest

# validate integers
def test_equal_or_not_equal():
    assert 3==3
    assert 3!=1

# validate instances
def test_is_instance():
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)

# validate Booleans
def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False

# validate types
def test_type():
    assert type('hello' is str)
    assert type('hello' is not int)

# validate greater than & less than
def test_greater_and_less_than():
    assert 3 > 2
    assert 2 < 3

# validate types
def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)

class Student:
    def __init__(self, firts_name: str, last_name: str, major:str, years: int):
        self.first_name = firts_name
        self.last_name = last_name
        self.major = major
        self.years = years

# def test_person_initalisation():
#     p = Student('John', 'Doe', 'Computer Science', 3)
#     assert p.first_name == 'John', 'First name should be John'
#     assert p.last_name == 'Doe', 'Last name should be Doe'
#     assert p.major == 'Computer Science', 'Major should be Computer Science'
#     assert p.years == 3, 'Years should be 3'

@pytest.fixture
def default_employee():
    return Student('John', 'Doe', 'Computer Science', 3)
def test_person_initalisation2(default_employee):
    assert default_employee.first_name == 'John', 'First name should be John'
    assert default_employee.last_name == 'Doe', 'Last name should be Doe'
    assert default_employee.major == 'Computer Science', 'Major should be Computer Science'
    assert default_employee.years == 3, 'Years should be 3'