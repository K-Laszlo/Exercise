from day5.inheritance.inheritance2.pet import Pet


class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):  # override
        print(f'Hello, my name is {self.name}, color: {self.color}')

    def speak(self):
        print('Meoooowwww')
