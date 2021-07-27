class Calculator:
    def __init__(self, num):
        self.num=num
    @staticmethod
    def greet():
        print("Hello Sir have a great Day!")
    def square(self):
        print(f"Square of {self.num} is ={self.num**2}")
    def squareRoot(self):
        print(f"Squareroot of {self.num} is ={self.num**0.5}")
    def cube(self):
        print(f"Cube of {self.num} is ={self.num**3}")
a=Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()