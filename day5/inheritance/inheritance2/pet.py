class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and {self.age} years old')

    def speak(self):
        print('Dont know what to say')
