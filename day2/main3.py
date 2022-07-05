age = 34
age2 = 14
# str_age = str(age)
# print('You are ' + str_age + ' years old')

# print formating from python 3.6
# print(f'You are {age} years old {age2}')


# name = 'John'
# age3 = 40
# greeting = 'Hello {}, you are {} years old'
# john_greeting = greeting.format(name, age3)
# print(john_greeting)

# name = 'Krisztina'
# age4 = 18
# greeting = 'Hello {n}, you are {a} years old'
# john_greeting = greeting.format(n=name, a=age4)
# print(john_greeting)

# build in functions

# word = 'hEllo'
# print(word.upper())
# print(word.lower())
# print(word.capitalize())
# print(word.startswith('h'))
# print(word.startswith('H'))
# print(word.endswith('o'))
# print(word.endswith('O'))

# my_number_list = [3, 2, 2, 50, -20, -30]
# # a = min(my_number_list)
# # print(a)
# #
# # print(max(my_number_list))
# #
# # print(sum(my_number_list))
#
# # my_number_list.sort()
# # print(my_number_list)
# #
# # my_str_list = ['z', 'a', 'b', 'c']
# # my_str_list.sort()
# # print(my_str_list)
#
# # my_number_list.reverse()
# # print(my_number_list)
# #
# # my_number_list.append(999)
# # print(my_number_list)
# #
# # my_number_list.insert(0, 999)  # elso parameter az index
# # print(my_number_list)
# # list2 = [2345, 23456, 45677]
# # my_number_list.insert(0, list2)  # elso parameter az index
# # print(my_number_list)
#
# # print(len(my_number_list))
#
# # print(my_number_list)
# # my_number_list.clear()  # Ures listank lesz a clear utan
# # list2 = [2345, 23456, 45677]
# # my_number_list.append(list2)  # elso parameter az index
# # print(my_number_list[0][1])
# #
# # print(49 not in my_number_list)
# # print(50 in my_number_list)
#
# my_number_list.remove(2)  # nem index alapjan hanem ertek alapjan torol.
# print(my_number_list)
#
# my_number_list.pop()  # Utolso elemet torli
# print(my_number_list)
#
# my_number_list.pop(0)  # index alapjan
# print(my_number_list)
#
# del my_number_list[1]  # index alapjan
# print(my_number_list)

# car_list = ['tesla', 'tesla', 'tesla', 'tesla', 'tesla', 'audi', 'trabant', 'tesla', 'bmw', 'tesla']
#
# counter = 1
# for car in car_list:
#     if car == ('tesla' + str(counter)):
#         print(car)
#         car_list.remove(car)
#         print(car_list)
#     counter += 1
#
# print(car_list)

# my_list = ["apple", "banana", "cherry", "dragonfruit", 'banana', 'banana', 'grape']
#
# counter = 0
# for fruit in my_list:
#     if fruit == "banana":
#         my_list.remove("banana")
#     print(fruit)
#     counter += 1


# no_tesla_list = []
# for car in car_list:
#     if car != 'tesla':
#         no_tesla_list.append(car)
#
# print(no_tesla_list)


# for car in car_list[:]:
#     if car == 'tesla':
#         car_list.remove(car)
#
# print(car_list)
#
# car = 'tesla'
# while car in car_list:
#     car_list.remove(car)
#
# print(car_list)

# my_number_list2 = [3, 2, 2, 2, 50, -20, -30]
# how_much = my_number_list2.count(2)  # Ertek
# # print(how_much)
#
# my_string = 'Hello World!'
# check = my_string.find('x')  # -1 ha nincs
# print(check)
# check2 = my_string.find('ll')  # 2. indexet kezdodik a keresett reszlet
# print(check2)

import math


# print(math.pow(2, 3))  # 2* 2 *2 = 8.0
# print(math.sqrt(9))  # 3.0   float


# def hello_world():
#     print('Hello')


# hello_world()


# def sum_two_number(number1, number2):
#     my_sum = number1 + number2
#     return my_sum
#
#
# result = sum_two_number(1, 5)
# print(result)
#
# print(sum_two_number('ab', 'cd'))


# age = 18
# if age <= 18:
#     print('you are young')
# else:
#     print('Lucky you are adult')
#
# age2 = 20
# if age2 <= 18:
#     print('you are young')
# else:
#     print('Lucky you are adult')
#
def is_adult(your_age):
    if your_age <= 18:
        print('you are young')
    else:
        print('Lucky you are adult')


# user_age = int(input('your age?'))
# is_adult(user_age)
# is_adult(20)
# is_adult(21)


# def greeting(name, age=0):
#     my_str = f'Hello {name}, you are {age} years old'
#     return my_str
#
# result = greeting('Krisztina', 18)
# print(result)


# def is_adult2(your_age):
#     is_adult = False
#     if your_age > 17:
#         is_adult = True
#     print(is_adult)
#     print(type(is_adult))
#     return is_adult
#
#
# result = is_adult2(21)
# print(result)

def check_string(new_word):
    print(new_word.startswith('a'))
    char_list = ['a', 'b']
    return char_list


l = check_string('almacica')
print(l)
