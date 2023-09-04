class colculator:
    def __init__(self,number):
        self.number = number
    def square(self):
        print(f"the value is {self.number} square is {self.number**2}")
    def squareroot(self):
        print(f"the value is {self.number} squareroot is {self.number**0.5}")
    def cube(self):
        print(f"the value is {self.number} cube is {self.number **3}")
a=colculator(9)
a.square()
a.squareroot()
a.cube()
