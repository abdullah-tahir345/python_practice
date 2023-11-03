# Protected variables are those varables in a class which is only accessible in the class and in the derived class.
# We can denote it it a single underscore.

# Base Class -- Parent Class -- Protected Variables
class Computer:
    # Make constructor for the class
    def __init__(self, processor, ram, hard_disk):
        self._processor = processor
        self._ram = ram
        self._hard_disk = hard_disk
        
    
# Derived Class -- Childern Class
class PC(Computer):
    def __init__(self, processor, ram, hard_disk, power_supply, VGA):
        self.power_supply = power_supply
        self.VGA = VGA
        super().__init__(processor, ram, hard_disk)
        
    def print_requirement(self):
        x = f"The PC requirements are {self._processor}, {self._ram}, {self._hard_disk}, {self.power_supply} and {self.VGA} VGA."
        return x
    
pc1 = PC('Core i5', 16, 1024, 9, 'supports')
print(pc1.print_requirement())

# As this is the protected variables in the derived class. So, we can override these functions. Let's check with an example
# For example our PC doesn't support the VGA. So, we will override it with "doesn't suppot"

pc1.VGA = "doesn't support"

#Let's print it
print(pc1.print_requirement())

# Also, We can access the protected variables through the derived class. Let's check it
print(f"\nHere's the protected variables, 1st variable is {{pc1._hard_disk}} and it's value is {pc1._hard_disk} and 2nd variable is {{pc1._processor}} and it's value is {pc1._processor} ")