class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def toString(self):
        return f"This vehicle is {self.color}"


#Example usage
veh1 = Vehicle('blue')
