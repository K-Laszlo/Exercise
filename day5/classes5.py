class Person:
    person_created = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_plus_one_to_counter()

    def __del__(self):
        print('DIED')

    @classmethod
    def add_plus_one_to_counter(cls):
        cls.person_created = cls.person_created + 1


person1 = Person('John', 14)
print(Person.person_created)
person2 = Person('John', 14)
print(Person.person_created)

my_list = []
my_list.append(person2)
my_list.append(person1)
my_list.append(123)
my_list.append('sadadsd')

del (person1)
