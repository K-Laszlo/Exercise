# Exercise: You will get list which contains a few dictionaries with a student name and a grade. Print out each of
# them nicely formatted sentence. "Name has a grade of X."
students = [
    {"name": "Jamal", "grade": 90},
    {"name": "Jay", "grade": 75},
    {"name": "Bob", "grade": 55},
    {"name": "Anne", "grade": 95}
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")

# Exercise: Collect and count the number in the list to a dictionary.
simple_list = [11, 45, 3, 8, 11, 23, 45, 23, 45, 89]

count_dict = dict()
for item in simple_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)

# Exercise:
new_dictionary = dict()
new_dictionary["ONE"] = 1
new_dictionary["TWO"] = 2
new_dictionary["THREE"] = 3
new_dictionary["FOUR"] = 4
# Add the key-value pair 'ONE-111', only if it the key is not present in dictionary
if "ONE" not in new_dictionary:
    new_dictionary["ONE"] = 111
# Add the key-value pair 'FIVE-5', only if it the key is not present in dictionary
if "FIVE" not in new_dictionary:
    new_dictionary["FIVE"] = 555

# Print the key-value pairs of dictionary
for key, value in new_dictionary.items():
    print(f"key: {key} value: {value}")
# Exercise 2:
new_dictionary2 = {
    111: 111.111,
    222: 222.222,
    333: 333.333,
    444: 444.444,
    555: 555.555
}
# Print the number of key-value pairs
print(len(new_dictionary2))
# Clear the dictionary
new_dictionary2.clear()
# Check the number of key-value pairs after clearing the dictionary
print(len(new_dictionary2))

# Exercise 3:
new_dictionary3 = dict()
new_dictionary3[1] = "AAA"
new_dictionary3[2] = "BBB"
new_dictionary3[3] = "CCC"
new_dictionary3[4] = "DDD"
new_dictionary3[5] = "EEE"
# Retrieve the keys from the dictionary and print it with for loop
for i in new_dictionary3.keys():
    print("key: " + str(i))

# Retrieve the values present in the dictionary and print them with for loop
for i in new_dictionary3.values():
    print("value: " + str(i))

# Exercise 4:
new_dictionary4 = {"ONE": "AAA", "TWO": "BBB", "THREE": "CCC", "FOUR": "DDD", "FIVE": "EEE"}
# Print the key-value pairs of the dictionary
for k, v in new_dictionary4.items():
    print(k, v)

# Remove the mapping for the key 'ONE'
del new_dictionary4["ONE"]
# Remove the mapping for the key 'THREE' only if it is currently mapped to 'DDD'
if new_dictionary4["THREE"] == "DDD":
    del new_dictionary4["THREE"]

# Remove the mapping for the key 'FIVE' only if it is currently mapped to 'EEE'
if new_dictionary4["FIVE"] == "EEE":
    del new_dictionary4["FIVE"]

# Print the key-value pairs of the dictionary
for k, v in new_dictionary4.items():
    print(k, v)

# Exercise 5:
new_dictionary5 = {"ONE": "AAA", "TWO": "BBB", "THREE": "CCC", "FOUR": "DDD", "FIVE": "EEE"}
# Replace the value associated with 'THREE' to '333'
new_dictionary5.update({"THREE": "333"})

# Replace the value associated with 'FOUR' to '444' only if it is currently mapped to 'DDD'
if new_dictionary5["FOUR"] == "DDD":
    new_dictionary5.update({"FOUR": "444"})

for k, v in new_dictionary5.items():
    print(k, v)
