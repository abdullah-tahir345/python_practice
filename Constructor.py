# Constructor is the special method/function which is used to intialize the instance/object attributes/variables.


# Constructor without parameter
class Computer(object): #Here we used object. Object is the parent class and Computer is it's parent class. Every class in python is the child of object class.
    def __init__(self): #Self is the keyword which shows the specific object. Self holds the address of specific object we are working on which object.
        self.processor = "Core i7"
        
    def show_specifications(self):
        print('Computer processor is :', self.processor)
        
comp = Computer()
comp.show_specifications()


# Constructor with parameter
class Computer:
    def __init__(self, processor, ram='16 GB'): #processor is formal parameter/argument and ram is default parameter/argument with value '16 GB'
        self.processor = processor
        self.ram = ram
        
    def show_specifications(self, hard_disk):
        print(f'Computer specifications are {self.processor}, {hard_disk} and {self.ram}.')


# Passing values to the constructor
comp = Computer('Core i7', '32 GB') # Here values are the actual parameter/argument   
# Passing values to the function from outside the class
comp.show_specifications('1024 GB')


