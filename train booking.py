class train():
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getstatus(self):
        print(f"the name of train is{self.name}")
        print(f"the seats available in train are {self.seats}")

    def fareinfo(self):
        print(f"the price of ticket:RS{self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"your ticket has been booked your seats number is {self.seats}")
            self.seats - self.seats-1
        else:
            print(f"sorry this train is full ! kindly try in next")
    def cancelticket(self,seatnumber):
        pass
express=train("express: 1400",1200,2)
express.getstatus()
express.bookTicket()

express.getstatus()
