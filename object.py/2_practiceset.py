class train:
    def __init__(self,name,fare,seats): # you can use any name instad of self but it is not good practice
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("***********************")
        print(f"The name of train is {self.name}")
        print(f"The fare of train is Rs {self.fare}")
        print(f"The seats of train is {self.seats}")
        print("***********************")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"The ticket has been booked!your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry this train is full!")


intercity=train("Rajdhani",200,45)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()    


