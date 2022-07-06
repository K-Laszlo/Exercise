# Exercise: you have a list. Remove all of the duplicated numbers and find the min, and max value in it. Do not use build in min, max functions!
sample_list = [13, 7, 1, 3, 45, 1, 5, 5, 7, 13, 2, 45]
sample_list = list(set(sample_list))

smallest = sample_list[0]
largest = sample_list[0]
for num in sample_list:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(smallest)
print(largest)

# Print out your friend name who likes art but no science.
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
art_but_no_science = art_friends.difference(science_friends)
print(art_but_no_science)
# Print out your friend name who likes science but no art;
science_but_no_friends = science_friends.difference(art_friends)
print(science_but_no_friends)

# Print out your friend name who likes marvel and dc universe as well.
marvel_fan = {"Jamal", "Joel", "Maria", "Tomislav"}
dc_fan = {"Joel", "Jamal", "Ervin", "Ivan"}
marvel_and_dc = marvel_fan.intersection(dc_fan)
print(marvel_and_dc)


# Exercise: Számoljunk átlagot egy iskolai órának (pl.: töri) a usertől bekért adatokkal.  Ahol lehet szervezzük ki külön metódusba a feladatokat.
# Kérd el a usertől a nevét majd üvdvözölt. (pl.: Hi Thomas)
# Kérj be egy számot.  Ez a szám fogja  megmutatni, hogy mennyi további számot kell bekérni a usertől.  (pl.: 5 , akkor 5 további számot fogunk bekérni)
# A fenti szám alapján kérjünk be egy annyi számot (osztályzatot) és mentsük el egy listába.  (pl.: 2, 2, 4, 5,1 )
# Számoljuk ki az átlagot
# Ha az átlag 2.5 alatt van, akkor dorgáljuk meg/ösztönözzük, hogy tanuljon többet, ha pedig felette akkor dícsérjük meg.

def ask_user_name():
    return input('What is your name?')


def how_many_number():
    return int(input('Ho many number rating do you have?'))


def your_rating(quantity_of_rates):
    marks = []
    for i in range(quantity_of_rates):
        marks.append(int(input('Your rating: ')))
    return marks


def count_avg(marks_list):
    list_length = len(marks_list)
    list_sum = sum(marks_list)
    avg = list_sum / list_length
    return avg


def check_avg(counted_avg):
    ret_str = ''
    if counted_avg < 2.5:
        ret_str = 'You should learn more'
    else:
        ret_str = 'You are safe now.'
    return ret_str;


user_name = ask_user_name()
print(f'Hi {user_name}')
marks_number = how_many_number()
user_marks = your_rating(marks_number)
usr_avg = count_avg(user_marks)
print(check_avg(usr_avg))
