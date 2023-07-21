# @property decorator called getter method
class employee:
    company="Bharat gas"
    salary=5600
    bonus=500

    @property                               # getter
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.setter
    def totalSalary(self,val):
      self.bonus=val-self.salary

e=employee()
print(e.totalSalary)   #print(e.totalSalary()) we also use this function call but call as property we use@property ex.print(e.totalSalary)
e.totalSalary=5800     #change total using setter
print(e.bonus)
print(e.salary)