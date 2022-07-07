def print_menu():
    print("0. Menu nyomtatása. \n"
          "1. Kocsi felvétel.  Adja meg a kocsi márkáját és alvázszámát \n"
          "2, Összes kocsi adatainak lekérdezese \n"
          "3, Kocsi adatainak lekérdezese index/key alapján. (márka, alvázszámát) \n"
          "4, Kocsi eladása \n"
          "5, Kilépés az applikáciobol")


def register_new_car():
    car_brand = input('What is the car brand?')
    serial = input('What is the car serial number?')
    tup = (car_brand, serial)
    return tup


def print_car_salon_car_list(cars):
    for key, value in cars.items():
        print(f'Car ID {key} brand: {value[0]} and serial: {value[1]}')


def print_car_by_index_or_key(car_salon, car_number):
    try:
        print(car_salon[car_number])
    except KeyError:
        print('This ID does not exists')


def sell_car(car_salon_cars, car_identifier):
    del car_salon_cars[car_identifier]
