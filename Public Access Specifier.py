# Public access specifiers are the variable method in which we can access the variable anywhere in the code.


# Base Class -- Parent Class
class Computer:
    # Make constructor for the class
    def __init__(self, processor, ram, hard_disk):
        # Public variables
        self.processor = processor
        self.ram = ram
        self.hard_disk = hard_disk
        
    
# Derived Class -- Childern Class -- Public Variables
class PC(Computer):
    def __init__(self, processor, ram, hard_disk, power_supply, VGA):
        self.power_supply = power_supply
        self.VGA = VGA
        super().__init__(processor, ram, hard_disk)
        
    def print_requirement(self):
        x = f"The PC requirements are {self.processor}, {self.ram}, {self.hard_disk}, {self.power_supply} and {self.VGA} VGA."
        return x
    
pc1 = PC('Core i5', 16, 1024, 9, 'supports')
print(pc1.print_requirement())

# As this is the public variables in the derived class. So, we can override these functions. Let's check with an example
# For example our PC doesn't support the VGA. So, we will override it with "doesn't suppot"

pc1.VGA = "doesn't support"

#Let's print it
print(pc1.print_requirement())

# Also, We can access the public variables anywhere in the code. Let's check it
print(f"\nHere's the public variables, 1st variable is {{pc1.hard_disk}} and it's value is {pc1.hard_disk} and 2nd variable is {{pc1.processor}} and it's value is {pc1.processor} ")