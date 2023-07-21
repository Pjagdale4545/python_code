class number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        print("let's add")
        return self.num+num2.num
    
    def __mul__(self,num2):
        print("let's multiply")
        return self.num*num2.num
    
    def __sub__(self,num2):
        print("let's substract")
        return self.num-num2.num
    
    def __truediv__(self,num2):
        print("let's divide")
        return self.num/num2.num
    
    def __floordiv__(self,num2):     #divide and returns integer removes ecimal
        print("let's floordiv")
        return self.num//num2.num
    
    
n1=number(4)
n2=number(6)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)
sub=n1-n2
print(sub)
truediv=n1/n2
print(truediv)
floordiv=n1//n2
print(floordiv)
