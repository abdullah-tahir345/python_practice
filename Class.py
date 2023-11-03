# Class is the blueprint of identical objects with methods and attributes.

class Computer:
    # Constructor
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram
        
    def print_requirements(self):
        print(f"PC requirements {self.processor} and {self.ram}.")
    
# This is used to check either the given source code is executable in the main program or not.
if __name__ == "__main__":
    # Make an object
    gaming_computer = Computer('Core i10', 32)
    gaming_computer.print_requirements()