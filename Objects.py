# Object of a class is a unique field that have some attribute and behaviour.

class Computer:
    # Constructor
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram
        
    def print_requirements(self):
        print(f"PC requirements {self.processor} and {self.ram}.")
    
# This is used to check either the given source code is executable in the main program or not.
if __name__ == "__main__":
    # Make an object 1 with the name of 'gaming_computer'
    gaming_computer = Computer('Core i10', 32)
    print('This is the output of 1st object.')
    gaming_computer.print_requirements()
    
    # Make an object 2 with the name of 'embaded_computer'
    embaded_computer = Computer('Core i5', 16)
    print('\nThis is the output of 2nd object.')
    embaded_computer.print_requirements()