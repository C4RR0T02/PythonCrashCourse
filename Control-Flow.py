# Control flow - how programs make decisions
# if block
if True:
    print("This code block runs if True")
    
# Example 1
# back to reservation robot
name = "Your Name"
age = 20

if name == "Your Name":
    print("Welcome customer!")
else: # run if statement above isn't true
    print("Go away you don't have a reservation")

name = "Kathleen"
age = 20

# if, else Statement
if name == "Your Name":
    print("Welcome customer!")
else: # run if statement above isn't true
    print("Go away you don't have a reservation")


# if, elif, else Statement
if name == "Your Name":
    print("Welcome customer!")
elif name == "Kathleen": # else if
    print("Welcome customer!")
# Useful if you want a default response
else: # run if statement above isn't true
    print("Go away you don't have a reservation")

# Example 2
# how do we make decision behind bringing umbrella out

isRaining = True
isSunnyAsHell = False

if isRaining or isSunnyAsHell:
    print("OK I'm gonna bring the umbrella out")
else:
print("No need bring lah")
