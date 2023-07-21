#salaryAfterIncreament=salary*increament

class employee:
    salary=1000
    increament=1.5

    @property                               # getter
    def salaryAfterIncreament(self):
        return self.salary * self.increament
    
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,val):
      self.increament=val/self.salary

e=employee()
print(e.salaryAfterIncreament)
e.salaryAfterIncreament=2000                  #change total using setter
print(e.increament)
print(e.salaryAfterIncreament)