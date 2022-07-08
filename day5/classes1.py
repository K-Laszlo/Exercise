class Person:

    def walk(self, name):
        print(f'I am walking {name}')


person1 = Person()
person1.name = 'Krisztina'
person1.age = 19

print(person1.name)

person1.walk('lajos')

person2 = Person()
print(person1)
print(person2)