

class freelancer:
    company="Google"
    level=0
    def upgardeLevel(self):
        self.level=self.level+1

class employee:
    company="TCS"
    eid="120"

class programmer(employee,freelancer):  # priority to first written class hence employee's company printed
    name="pooja"

p=programmer()
p.upgardeLevel()
print(p.level)
print(p.company)   


