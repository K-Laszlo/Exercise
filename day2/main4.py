# print('a')
# print('b')
# print(c') # syntax error


# print(10 * (1 / 0)) # ZeroDivisionError
# 4 + dog * 3 # NameError
# print('2' + 2) # TypeError

# try:
#     numerator = 5
#     denominator = 0
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print('denominator can not be 0')
#
# print('Hello Class')


# try:
#     numerator = 5
#     denominator = 0
#
#     result = numerator / '2'
#     print(result)
# except ZeroDivisionError:
#     print('denominator can not be 0')
# except NameError:
#     print('Dog not be found')
# except TypeError:
#     print('can not be do sh')
# except BaseException:
#     print('something else')
#
# print('Hello Class')

try:
    numerator = 5
    denominator = 0

    result = numerator / 5
    print(result)
except ZeroDivisionError:
    print('denominator can not be 0')
finally:
    print('Finnaly ag')

print('Hello Class')
