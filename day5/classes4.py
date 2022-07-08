class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # User friendly
        return f'{self.name} is {self.age} years old'

    def __repr__(self): # developer friendly
        return f"Person('{self.name}', {self.age})"


person1 = Person('John', 14)
print(person1)
print(person1.__repr__())

pers2 = Person('John', 14)