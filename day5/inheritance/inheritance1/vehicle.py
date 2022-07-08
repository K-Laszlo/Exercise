class Vehicle:  # Parent class

    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def make_sound(self):
        print('Brummmmmbrummmmm')
