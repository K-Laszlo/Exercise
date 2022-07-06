# SET unions stb.

lettersA = {"A", "B", "C", "D"}
lettersB = {"D", "E", "F"}

# Set Union. It puts together the two set. Order is still not guaranteed
union = lettersA | lettersB
print(f"Union = {union}")

union2 = lettersA.union(lettersB)
print(f"Union2 = {union2}")


# Set intersection. It gives back that thing what you can find in both  set.
intersection = lettersA & lettersB
print(f"Intersection = {intersection}")

intersection2 = lettersA.intersection(lettersB)
print(f"Intersection2 = {intersection2}")

# Set difference. It gives back that elements which you can not find one of the set.
difference1 = lettersA - lettersB
difference2 = lettersA.difference(lettersB)
print(f"Difference1 = {difference1}")
print(f"Difference2 = {difference2}")

difference3 = lettersB - lettersA
difference4 = lettersB.difference(lettersA)
print(f"Difference3 = {difference3}")
print(f"Difference4 = {difference4}")


# Set symmetric. It gives back that elements that are not in both sets.
symmetric = lettersA ^ lettersB
print(f'Symmetric: {symmetric}')


symmetric2 = lettersA.symmetric_difference(lettersB)
print(f"Symmetric: {symmetric2}")

print("________________")