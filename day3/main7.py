# # Tuple
# numbers_list = []
# numbers_set = {}
# numbers_tuple = (21, -5, 6, 9, 9)
# # print(numbers_tuple)
# # print(numbers_tuple[0])
# # print(numbers_tuple[1])
# # print(numbers_tuple[0:3])
#
# # for i in numbers_tuple:
# #     print(i)
# # num_tuple_to_list = list(numbers_tuple)
# # numbers_tuple[0] = 95  # Nem engedi modositani
# print(numbers_tuple)
#
# friends = ('Rolf', 'Bob', 'Anne')
# friends2 = friends + ('Anne', 'John')
# print(friends2)

# Dictionary
person = {
    'name': 'Tommy',
    'age': 25,
    'address': 'USA',
}

# new_dict = {  # ne igy hozzunk letre ures dictionaryt
#     '': ''
# }
#
# new_dict2 = dict()  # good practise

# print(person['name'])
# print(person['age'])
#
# print(person.get('name'))

# print(person.keys())
# print(person.values())
# Add new key value pair
# person['street'] = 'Hos utca'
# print(person)
#
# my_street = person.pop('street')  # return value
# print(person)
# print(my_street)
#
# person['street'] = my_street
# print(person)
#
# # Delete key value pair
# del person['street']
# print(person)

# print(person.get('age'))
# person['age2'] = 18
# print(person.get('age'))
# print(person)
# person.update({'age': 5})
# print(person)

# for k in person:
#     print(f'Keys: {k}')
#
# for k in person.keys():
#     print(f'Keys: {k}')
#
# for v in person.values():
#     print(f'Values: {v}')

for k, v in person.items():  # key value iteration
    print(f'Keys: {k} Values: {v}')

for k in person.keys():  # key iteration  but we can ask out the value from person.
    print(f'Keys: {k} Values: {person[k]}')
#
# person.clear()  # Dictionary megmarad de ures lesz.
# print(person)

my_list = [1, 2, 3]
person['music'] = my_list
print(person['music'][1])