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

name = 'Krisztina'
age4 = 18
greeting = 'Hello {n}, you are {a} years old'
john_greeting = greeting.format(n=name, a=age4)
print(john_greeting)