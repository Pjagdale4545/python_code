# single inheritence - one child class inherits from one base class

class employee:               #parent class
    company="google"
    language="java"
    def getDetails(self):
        print(f"This is an employee from {self.company}")
        print(f"This is  {self.language} language")

class programmer(employee):      # child/derived clss
    language="python"            #overriding print python
   
    def getLanguage(self):
        print(f"This is  {self.language} language")
        
    def getDetails(self):
        print("This is a programmer")

e=employee()
e.getDetails()

p=programmer()
p.getLanguage()
p.getDetails()
print(p.company)

