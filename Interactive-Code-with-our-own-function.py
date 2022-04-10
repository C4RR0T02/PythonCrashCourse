# Defining our own functions
# define a function that returns True or False depenfing on input

# format to define function
# def [function name]([input to take in]):
#     if [condition]:
#       [action to be performed]
#     else:
#       [action to be performed]

# To call the function
# [function name]([input to take in])


name = input("What is your Name: ")
age = int(input("What is your age: "))

def barRobot(userAge):
    if userAge >= 18:
        return "Ok I let you pass"
    else: 
        return "Oh no you're too young"

print(barRobot(age))

# Why use return instead of print
# -> To store the value

response = barRobot(age)

print("The robot said", response)
