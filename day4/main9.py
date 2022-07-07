# Olvasas regi megkozelites

# my_text = open('data.txt', 'r', encoding='UTF-8')
# my_content = my_text.read()
# my_text.close()  # Lezarni!!!
# print(my_content)
# # print(type(my_content))

# Olvasas uj megkozelites
#
# with open('data.txt', 'r', encoding='UTF-8') as my_text2:
#     my_content2 = my_text2.read()
#     print(my_content2)
#     # Nem kell lezarni

user_input = input('Neved?')

# with open('data.txt', 'w', encoding='UTF-8') as file:
#     file.write(user_input) # Torli a file tartalmat majd beleirja az uj adatot

# with open('data.txt', 'a', encoding='UTF-8') as file:
#     file.write('\n')
#     file.write(user_input)


try:
    with open('data2.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Could not find this file')
