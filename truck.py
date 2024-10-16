from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer
    
    def toString(self):
        return f"{super().toString()}\nHas trailer: {self.has_trailer}"


#Example Usage
print('...............truck1 info...............')
print('........................................................')
truck1 = Truck('Orange', True)
print(truck1.toString())

print('\n******************************************************\n')

print('...............truck2 info...............')
print('........................................................')
truck2 = Truck('Green')
print(truck2.toString())