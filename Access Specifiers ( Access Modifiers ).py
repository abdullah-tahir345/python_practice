# Access specifiers/Access modifiers are the keywords used in OOP (Objects oriented programming) which controls the 
# accessibilty of class members, contructors and variables.

# Parent Class -- Base Class
class Computer:
    # Constructor
    def __init__(self, processor, ram, hard_disk):
        # Access Specifier -- Public
        self.processor = processor
        # Access Specifier -- Protected
        self._ram = ram
        # Access Specifier -- Private
        self.__hard_disk = hard_disk
        
    def print_requirements(self):
        # Here we have used the access specifiers in this function of class
        print(f"PC requirements {self.processor}, {self._ram} and {self.__hard_disk}.")
    
# Child Class -- Derived Class
class Gaming_Computer(Computer):
    # Constructor
    def __init__(self, processor, ram, hard_disk, graphics_card):
        super().__init__(processor, ram, hard_disk)
        # Access Specifier -- Public
        self.graphics_card = graphics_card
        
    def print_requirements_child(self):
        # Here we have used the access specifiers in this function of class
        print(f"PC requirements {self.processor}, {self._ram}, {{self.__hard_disk(If we use this private variable it'll cause an error')}} and {self.graphics_card}")
    
# This is used to check either the given source code is executable in the main program or not.
if __name__ == "__main__":
    # Make an object
    embaded_computer = Computer('Core i10', 32, '1024 GB')
    embaded_computer.print_requirements()
    
    #Make an object of child class
    gaming_computer = Gaming_Computer('Core i10', 32, '1024 GB', '1GB')
    gaming_computer.print_requirements_child()
    
    # Access the public access variable
    print('Public Access Specifiers Value :',embaded_computer.processor)
    
    # Access the protected access variable
    print('Protected Access Specifiers Value :',embaded_computer._ram)
    
    # Access the private access variable : If we run this line of code this will cause an error because private variable
    # are only inaccessible outside the class.
    # print('Private Access Specifiers :',embaded_computer.__hard_disk)
    
    # But python provide us a technique through which we can access the private variables outside the class and this 
    # technique is called mangling. But it's not a good practice.
    print('Private Access Specifiers Value Using Mangling :',embaded_computer._Computer__hard_disk)