"""
inheritance is all about DRY, don't repeat
Just like baseException, all exception inherits it
Just like object class, all class inherits it
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be an empty string")
        self._name = value.capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value


class Human(Animal):
    def __init__(self, name, age, profession):
        """
        This is the most important thing, you must also call the base class constructor manually
        It's not called automatically in python
        This is called method extension
        """
        super().__init__(name, age)
        self.profession = profession

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        if not isinstance(value, str):
            raise TypeError("Profession must be a string")
        if value == "":
            raise ValueError("Profession cannot be an empty string")
        self._profession = value.capitalize()

    def __str__(self):
        return f"{self.name} {self.age} {self.profession}"


arafat = Human("arafat", 29, "engineer")
print(arafat)
print(isinstance(arafat, Human))
print(isinstance(arafat, Animal))
"""
All classes in python is derived from default object class
Any class inherits from object
All magic methods defined there, some implemented others are not
"""
print(isinstance(arafat, object))

"""
We also have multi level inheritance, also its generally advice to avoid multiple inheritance
This also introduces the dimond problem
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()

Output
Hello from D
Hello from B
Hello from C
Hello from A

Python uses MRO (Method Resolution Order), C3 linearization algo, advanced stuff google up

There is also multiple inheritance
class Parent1:
    def method_a(self):
        print("Method A from Parent1")

class Parent2:
    def method_b(self):
        print("Method B from Parent2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method_a()  # Method A from Parent1
c.method_b()  # Method B from Parent2

Incase of a conflict, same MRO is used, google up
"""
