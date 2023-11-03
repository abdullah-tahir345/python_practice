class Computer:
    def __init__(self, brand:str, model:int, processor:str, ram_size:str, storage_capacity:str, operating_system:str):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram_size = ram_size
        self.storage_capacity = storage_capacity
        self.operating_system = operating_system
        
    def start(self):
        return "It's booting up."
    
    def shutdown(self):
        return "It's powering off."
    
    def display_info(self):
        return f"Computer information\nBrand : {self.brand}\nModel : {self.model}\nProcessor : {self.processor}\nRam Size : {self.ram_size}\nStorage Capacity : {self.storage_capacity}\nOperating System : {self.operating_system}"
    
    
if __name__ == '__main__':
    com1 = Computer('Intel', 2011, 'Core i7', '16GB', '1024GB', 'Windows')
    print(com1.start())
    print()
    print(com1.display_info())
    print()
    print(com1.shutdown())
    
    
    