# superclass
class person:
    country="India"
    def __init__(self):
        print("initializing person ...\n")
    def takebreadth(self):
        print("I am breathing....")

class employee(person):
    company="Honda"
    def __init__(self):
        super(). __init__()
        print("initializing employee....\n ")
    def getSalary(self):
        print(f"salary is {self.salary}")

    def takebreadth(self):
        super().takebreadth()
        print("I employee breathing....")

class programmer(employee):
    company="TCS"
    def __init__(self):
        super(). __init__()
        print("initializing programmer....\n ")

    def getSalary(self):
        print("No salary for programmer")
    
    def takebreadth(self):
        super().takebreadth()
        print("I am programmer also breathing....")

# p=person()
# p.takebreadth()
# e=employee()
# e.takebreadth()
pr=programmer()
pr.takebreadth() 



 


