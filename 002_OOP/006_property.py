"""
How we set up getters and setters in a pyhon attribute
"""
from logging import exception


class Person:
    def __init__(self, name, age):
        self.name = name
        # We are making age mangle, want to reduce exposure
        self.set_age(age) # self.__age = age -> This is bad, wrong. If you save setters always must use them
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 18:
            self.__age = age
        else:
            raise ValueError('age must be greater than 18')

    '''
    But the above example is unpythonic way, sucks. There is a better way to do it in python. Using property
    '''
arafat = Person('Arafat', 20)
print(arafat.get_age())
arafat.set_age(21)
print(arafat.get_age())


'''
More Pythonic way, using property
'''
class PersonUpdated:
    def __init__(self, name, age):
        self.name = name

        # This goes through the property, not assigned directly
        # because age is a property
        self.age = age
    @property
    def age(self): #function must be names as property
        return self.__age
    @age.setter
    # again, function name always should be property name
    def age(self, age):
        if age >= 18:
            self.__age = age
        else:
            raise ValueError('age must be at least 18')
    @age.deleter
    def age(self):
        # This prevents us from deleting the age field like 'del object.age'
        raise ValueError('Age cannot be deleted')
try:
    arafat = PersonUpdated('Arafat', 16)
except ValueError as e:
    print("Encountered error creating arafat:", e)

arafat = PersonUpdated('Arafat', 20)
print(arafat.age)
arafat.age = 21
print(arafat.age)

try:
    del arafat.age
except ValueError as e:
    print("Encountered error deleting arafat's age:", e)

'''
If we have only getters, the property cannot be updated after object construction
But you need to write all the settler logic inside __init__ and it will only run once

'''

class ImmutablePerson:
    def __init__(self, name, age):
        self.name = name
        if age < 18:
            raise ValueError('age must be at least 18')
        self._age = age  # We good, name mangling overkill you cannot set it anyways

    @property
    def age(self):
        return self._age

arafat = ImmutablePerson('Arafat', 20)
print(arafat.age)
try:
	arafat.age = 21
except BaseException as e:
	print("Encountered error updating age:", e)