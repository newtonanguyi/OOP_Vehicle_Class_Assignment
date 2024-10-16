from truck import Truck
from garage import Garage

class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck("black", False)
        garage = Garage()
        garage.setVehicle(truck)

        print(garage )

# Example usage
GarageTester.getExample()