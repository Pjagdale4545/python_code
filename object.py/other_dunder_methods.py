class number:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):        #used to set what displayed on calling len()
        return 1
    
n=number(99)
print(n)
print(len(n))