class calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2} ")
        
    def squareroot(self):
        print(f"The value of {self.number} squareroot is {self.number **3} ")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **0.5} ")
    
    @staticmethod
    def greet():
        print("**************welcome to the best calculator of the world*****************")

a=calculator(3)
a.greet()
a.square()
a.squareroot()
a.cube()



