cars = ['Audi', 'Tesla', 'Trabant', 'Bwm']

# My is is Audi and index is 0.

# for index in range(len(cars)):
#     print(f'My is {cars[index]} and index is {index}.')

# counter = 0
# for car in cars:
#     print(f'My is {car} and index is {counter}.')
#     counter += 1

for index, car in enumerate(cars):
    print(f'My is {car} and index is {index}.')

for index, car in enumerate(cars, start=1):
    print(f'My is {car} and index is {index}.')
