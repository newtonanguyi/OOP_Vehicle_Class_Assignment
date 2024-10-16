class Garage:
    def __init__(self):
        self.parked_vehicle = None
    
    def setVehicle(self, vehicle):
        self.parked_vehicle = vehicle
    
    def toString(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle}"
        else:
            return "The garage is empty."

print("............garage1 info.............")
garage1 = Garage()
garage1.setVehicle('Toyota Hilux')
print(garage1.toString())

print('\n******************************************************************\n')

print("............garage2 info.............")
garage2 = Garage()
garage2.setVehicle(None)
print(garage2.toString())