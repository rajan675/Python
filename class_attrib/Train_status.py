class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getInfo(self):
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is Rs  {self.fare}")
        print(f"The Number  of  seats abilabe in the train is {self.seats}")

    @staticmethod
    def greet():
        print("Hello Sir!")

    def bookTickets(self):
        if self.seats>0:
            print(f"Your seat  number is {self.seats} ")
            self.seats= self.seats-1
        else :
            print("Sorry! The Train is Full")
a=Train("Intercity Express", 300, 5)
a.greet()
a.bookTickets()
a.bookTickets()
a.getInfo()
