class Person:
    younger_rate = 0.8  # osztalyvaltozo

    def __init__(self, name, age):
        self.name = name  # peldanyvaltozo
        self.age = age
        self.magic_potion = False

    def make_me_younger(self):
        # if not self.magic_potion:
        if self.magic_potion == False:
            self.age = self.age * Person.younger_rate
            self.magic_potion = True
            print(f'Your age is {self.age}')
        else:
            print('You have already used this potion.')


person1 = Person('Krisztina', 20)
print(person1.age)
person1.make_me_younger()
person1.make_me_younger()
print(person1.age)
