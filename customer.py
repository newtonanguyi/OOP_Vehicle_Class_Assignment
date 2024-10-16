class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def toString(self):
        return f"Customer name: {self.name}, Address: {self.address}"


cust1 = Customer('John', 'Kasese')
print(cust1.toString())
