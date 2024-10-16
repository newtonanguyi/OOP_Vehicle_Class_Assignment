from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires
    
    def toString(self):
        return f"{super().toString()}\nHas winter tires: {self.has_winter_tires}"


car1 = Car('blue', True)
print(car1.toString())