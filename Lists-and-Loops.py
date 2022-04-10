# Learning about lists
# list is a form of array
# array is a collection of things
letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]

print(letters)
print(numbers)

# Retrieve item in list using indexing
# index = position
# Counting starts from 0 in python

#   0    1    2    3    4
# ["a", "b", "c", "d", "e"]

print(letters[3])

# What is I want to have ["b", "c"]
# Use slicing
# my_list[start_index : end_index + 1]

print(letters[1 : 3])

# Start from the start (slicing)
print(letters[:3])
# End at the end (slicing)
print(letters[1:])

# Loops

# ["a", "b", "c", "d", "e"]
# Use a for loop to loop through arrays
for placeholder in letters:
    print(placeholder)
    

# while some_condition:
#   run this code until some_condition is not valid

age = 12
while age < 18:
    print("You cannot drink")
    age += 1 # += means increment variable by some value
