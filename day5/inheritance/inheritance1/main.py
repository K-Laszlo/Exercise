from day5.inheritance.inheritance1.bus import Bus
from day5.inheritance.inheritance1.car import Car

school_bus = Bus('Volvo bus', 100, 15000)
school_bus.make_sound()

print(Bus.color, school_bus.name, school_bus.max_speed, school_bus.mileage)

car = Car('Audi', 200, 150000)
print(car.color, car.name, car.max_speed, car.mileage)