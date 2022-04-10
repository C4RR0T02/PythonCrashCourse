# Object Oriented Programming (OOP)
# think of the Class as a blueprint
# think of an object as something built from the blueprint

class Person:
    def __init__(self, given_name, given_age, given_quote):
        # Set attributes (properties)
        self.name = given_name
        self.age = given_age
        self.quote = given_quote
        
    # defined method
    def sayHelloWorld(self):
        print("Hello World!")
    
    #define a method called sayAge where the object would say its own age
    def sayAge(self, age):
        print("My age is", self.age)
        
    def sayQuote(self, given_quote):
        print(self.quote)
    
P1 = Person("Kathleen", 20, "Its never too late to learn how to code!")
print("Hi, I'm", P1.name, "and I am", P1.age, ". My quote to you is", P1.quote)
