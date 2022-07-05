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
# 0         1       2       3           4       5           6       7       8
car_list = ['tesla', 'tesla', 'tesla', 'tesla', 'tesla', 'audi', 'trabant', 'tesla', 'bmw', 'tesla']

"""
audi tesla, tesla, tesla tesla, tesla, trabant
audi tesla tesla tesla, tesla, trabant
audi teslam tesla, tesla, trabant
"""

# counter = 1
# for car in car_list:
#     if car == ('tesla' + str(counter)):
#         print(car)
#         car_list.remove(car)
#         print(car_list)
#     counter += 1
#
# print(car_list)


# no_tesla_list = []
# for car in car_list:
#     if car != 'tesla':
#         no_tesla_list.append(car)
#
# print(no_tesla_list)


for car in car_list[:]:
    if car == 'tesla':
        car_list.remove(car)

print(car_list)

car = 'tesla'
while car in car_list:
    car_list.remove(car)

print(car_list)


