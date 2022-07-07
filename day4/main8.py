my_list1 = ['alma', 'korte', 'repa', 'cseresznye']
my_list2 = [1, 2, 3, 4]

# for i in my_list1:
#     for k in my_list2:
#         print(f'Fuit {i} and number {k}')
"""
....0
...00
..000
.0000
"""

n = 4
for row in range(n):  # 0 1 2 3
    for column in range(n-row):
        print('.', end='')
    for column2 in range(row + 1):
        print('0', end='')

    print()


"""
....0....
...000...
..00000..
.0000000.
"""