import hashlib


class Person:
    def __init__(self, name, age, social_security_number):
        self.name = name
        self.age = age
        self.social_security_number = social_security_number

    def __str__(self):
        return f"{self.name}:{self.age}:{hashlib.sha1(self.social_security_number.encode('utf-8')).hexdigest()}"


arafat = Person("Arafat", 26, "AX79DKE41")

print(arafat)
# But there is a security issue, anyone can access arafat's social number
print(
    "Printing arafat's social security number:", arafat.social_security_number
)  # Security issue


# Lets build our improved class with social security mangled
class PersonImproved:
    def __init__(self, name, age, social_security_number):
        self.name = name
        self.age = age
        # This is called name mangling, it's still accessible but harder
        # prefix with double underscore
        # Not exaclty private but makes it harder
        self.__social_security_number = social_security_number

    def __str__(self):
        return f"{self.name}:{self.age}:{hashlib.sha1(self.__social_security_number.encode('utf-8')).hexdigest()}"


secured_arafat = PersonImproved("Arafat", 26, "AX79DKE41")
try:
    print("Trying to print secured arafat's social number")
    print(
        f"{secured_arafat.__social_security_number}"
    )  # Runtime Error: AttributeError: 'PersonImproved' object has no attribute '__social_security_number'
except AttributeError as e:
    print("Caught Exception" + e.__str__())


"""
The way mangling happens, obj.attribute -> obj._ClassName__attribute
so our secured_arafat.__social_security_number becomes secured_arafat._PersonImproved__social_security_number
also magic attribute __dict__ holds all the attributes of the person, so nothing is really private here. You can see the mangling in action from dict
"""

print(
    "Escaping name mangling, printing arafat's social number:",
    secured_arafat._PersonImproved__social_security_number,
)

print(secured_arafat.__dict__)
