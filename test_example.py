# from atk import attack_damage
# from unittest import mock

from people import Person, anyone_likes_dogs

import pytest
# ---------------------------------------------------------------

# def test_pass():
#     assert 1 + 1 == 2

# def test_fail():
#     assert 2 + 2 == 5

# ---------------------------------------------------------------

# def greet(person):
#     return "Hi {name}".format(**person)

# def test_greet():
#     bob = {"name": "Bob"} #Arrange
#     greeting = greet(bob) #Act
#     assert greeting == "Hi Bob" #Assert 

#---------------------------------------------------------------

# @mock.patch("atk.randint", return_value=5, autospec=True)

# def test_attack_damage(mock_ranint):
#     assert attack_damage(1) == 6
#     mock_ranint.assert_called_once_with(1,8)

#---------------------------------------------------------------

@pytest.fixture()

def person(**kwargs):
    count = 0
    def _person(**kwargs):
        nonlocal count
        count += 1
        name = kwargs.pop("name","Bob {}".format(count))
        return Person(name=name, **kwargs)

    return _person

def test_anyone_likes_dogs_true(person):
    people = [
        person(favorite_animal="cat"), 
        person(favorite_animal="dog")
        ]
    assert anyone_likes_dogs(people) is True

def test_person(person):
    assert person().name != person().name 
    assert person(name="Alice").name == "Alice"