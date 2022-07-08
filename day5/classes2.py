class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.active = True


    def walk(self, email):
        print('I am walking', self.name, self.age, email)


person1 = Person('Krisztina', 20)
person2 = Person('John', 20)

print(person1)
print(person2)
# Person('John', 45)  # garbage collector ezt el fogja takaritani egy ido utan.
#
person1.walk('a@gmail.com')
