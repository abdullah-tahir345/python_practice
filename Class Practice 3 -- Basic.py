class Product:
    # Make constructor
    def __init__(self, name, price:int):
        self.name = name
        self.price = price
        self.quantity_available = 0
    
    # Make method of add inventory
    def add_to_inventory(self, quantity):
        if quantity > 0:
            self.quantity_available = self.quantity_available + quantity
            return f'New Quantity : {self.quantity_available}'
        else:
            return 'Invalid Quantity'
    
    # Make method of check availability product
    def check_availability(self):
        if self.quantity_available > 0:
            return f'Product is Available {self.quantity_available}'
        else:
            return 'Product not available'
    
    # Make purchase method
    def make_purchase(self, quantity:int):
        if quantity > 0:
            if self.quantity_available > quantity:
                actual_quantity = self.quantity_available
                self.quantity_available = self.quantity_available - quantity
                bill = self.price * quantity
                return f"Your actual quantity is {actual_quantity} and {quantity} is deducted from your stock.And your bill is {bill}."
            elif self.quantity_available < quantity:
                return "Quantity Not Available"
        else:
            return 'Invalid Quantity'
        
if __name__ == "__main__":
    # Make object of lays product
    lays = Product('Lays', 60)
    print(lays.add_to_inventory(100))
    
    # Make some purchase and check product avaiablility
    print(lays.check_availability())
    print(lays.make_purchase(2))
    print(lays.make_purchase(8))
    print(lays.check_availability())
    
    print()
    
    # Make object of neutella product
    neutella = Product('Neutella', 1400)
    print(neutella.add_to_inventory(20))
    
    # Make some purchase and check product avaiablility
    print(neutella.check_availability())
    print(neutella.make_purchase(1))
    print(neutella.check_availability())
    
    print()
    # Invalid Quantity
    print(neutella.make_purchase(-100))
    