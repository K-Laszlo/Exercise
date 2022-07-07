# Exercise:
# Egy autókereskedés belső szoftware-t szeretnénk megcsinálni. Egy kocsinak

# - Írjunk egy programot, ami induláskor nyomtat nekünk egy menüt.
#   0. Menu nyomtatása.
#   1. Kocsi felvétel.  Adja meg a kocsi márkáját és alvázszámát.
#   2, Összes kocsi adatainak lekérdezese
#   3, Kocsi adatainak lekérdezese index/key alapján. (márka, alvázszámát)
#   4, Kocsi eladása (töröljük a rendszerből egy kocsit)
#   5, Kilépés az applikáciobol

# -

from car_salon_methods import *

flag = True
car_salon_cars = dict()
counter = 0

print_menu()
while flag:
    try:
        user_input = int(input('What would you like to do?'))
        if user_input == 0:
            print_menu()
        elif user_input == 1:
            car_salon_cars[counter] = register_new_car()
            counter += 1
        elif user_input == 2:
            print_car_salon_car_list(car_salon_cars)
        elif user_input == 3:
            car_number = int(input('Which car details do you need?'))
            print_car_by_index_or_key(car_salon_cars, car_number)
        elif user_input == 4:
            car_identifier = int(input('Which car do you sell?'))
            sell_car(car_salon_cars, car_identifier)
        elif user_input == 5:
            print('Thanks for using XY software')
            flag = False
        else:
            print('This menu does not exists.')
    except ValueError:
        print('Use a number please')
