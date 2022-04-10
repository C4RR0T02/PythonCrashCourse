# Make our code interactive

#variable = input(prompt to get info from user)
name = input("What is your name? ")
# Getting the age input as an integer
age = int(input("What is your age? "))

print("Your name is", name, "and your age is", age, "years old")
print("You are born in", 2022 - age)

#getting the age input as a string before converting it to an integer
age = input("What is your age? ")

print("Your name is", name, "and your age is", age, "years old")
print("You are born in", 2022 - int(age))

# use int() to convert values to int 
# similarly for other data types
