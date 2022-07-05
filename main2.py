car1 = 'Tesla'
car2 = 'Trabant'
car3 = 'Audi'

# cars = ['Tesla', 'Trabant', 'Audi']
# print(len(cars))  # length
# print(cars[0])
# print(cars[1])
# print(cars[2])

# list_mixed = [2, 3, False, 'Dog']
# list_homogeneous = [2, 3, 4, 5, 6, 7]


# cars = ['Tesla', 'Trabant', 'Audi', 'Bmw', 'Ford', 'Ferrari']
# sliced_cars = cars[1:4]  # excluded a 2. szám
# print(sliced_cars)

# sliced_cars2 = cars[2:]
# print(sliced_cars2)
#
# sliced_cars3 = cars[:3]
# print(sliced_cars3)
# sliced_cars4 = cars[-2:]
# print(sliced_cars4)
# sliced_cars5 = cars[:-3]
# print(sliced_cars5)

# sliced_cars6 = cars[:]
# print(sliced_cars6)
#
# my_str = 'Little Dog'
# print('darab', len(my_str))
# print('index', len(my_str)-1)
# print(my_str[1:3])


# Forloop

cars = ['Tesla', 'Trabant', 'Audi', 'Bmw', 'Ford', 'Ferrari']

# for car in cars:
#     print(car + " ", end='')

# for car in cars:
#     print(car.upper())

# for car in cars:
#     if car == 'Tesla':
#         print('Nyeeeeehh')
#     else:
#         print('Cool car')

# number_list = range(10)  # [0,1,2,3,4,5,6,7,8,9]
#
# for num in number_list:
#     if num % 2 == 0 and num != 0:
#         print(str(num) + ' ', end='')

# num_list = range(2, 20)
# for num in num_list:
#     print(num)

# num_list = range(2, 20, 3)
# for num in num_list:
#     print(num)

# break/continue

# for num in range(30):
#     if num == 5:
#         print('I have reached number 5')
#         break  # For loopot megtori/kilep
#         print('After break')
#     print(num)

# for num in range(30):
#     if num == 5:
#         print('I have reached number 5')
#         continue
#         print('After continue')
#     print(num)


# While loop
number = 1
while number < 10:
    print('OK')
    number += 1
    #number = number + 1

for_while_loop = True
while for_while_loop:
    pass

import random

my_number = random.randint(0, 11)
user_input = -1
while my_number != user_input:
    user_input = int(input("Enter your number:"))
    if my_number == user_input:
        print("Yeeees, You won this round!")
    else:
        print("Noooo, try again!")