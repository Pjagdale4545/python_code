# MULTILEVEL Inheritance-when child class become parent for another child class
class person:
    country="India"
    def takebreadth(self):
        print("I am breathing....")

class employee(person):
    company="Honda"
    def getSalary(self):
        print(f"salary is {self.salary}")

    def takebreadth(self):
        print("I employee breathing....")

class programmer(employee):
    company="TCS"
    def getSalary(self):
        print("No salary for programmer")

p=person()
e=employee()
pr=programmer()
pr.getSalary()
p.takebreadth()
e.takebreadth()
pr.takebreadth() 
print(e.company) 
#print(p.company)  throw arror 
print(p.country)
print(e.country)
print(pr.country)
