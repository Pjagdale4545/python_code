#classmethod is for change the class attribute
class employee:
    company="camel"
    salary=100
    loaction="delhi"
    
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

    # def changeSalary(self,sal):
    #     self.salary=sal
    
e=employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(employee.salary)     # this is change only after using @classmethod before this it prints 100