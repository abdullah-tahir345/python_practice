# Private variables are those varables in a class which is only accessible in the class and not in the derived class or not anywhere.
# We can denote it it a double underscore.

# Base Class -- Parent Class -- Private Variables
class Computer:
    # Make constructor for the class
    def __init__(self, processor, ram, hard_disk):
        self.__processor = processor
        self.__ram = ram
        self.__hard_disk = hard_disk
    
    def print_requirement(self):
        x = f"The PC requirements are {self.__processor}, {self.__ram} and {self.__hard_disk}."
        return x
        
    
pc1 = Computer('Core i5', 16, 1024)
print(pc1.print_requirement())

# As this is the protected variables in the derived class. So, we can override these functions. Let's check with an example
# For example our Computer have Core i7 processor. So, we will override it with "Core i7"

# But this will throw an error because this is the private variable and not accessible anywhere.
# pc1.__processor = "Core i7"

#Let's print it
print(pc1.print_requirement())
