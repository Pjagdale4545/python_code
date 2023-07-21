#craete 2Dvector class AND USE IT TO CREATE 3D VECTOR  check on google vector diagram

class C2dVec:
    def __init__(self,i,j):
       self.icap=i
       self.jcap=j

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"

       
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
    #    self.icap=i
    #    self.jcap=j
       super().__init__(i,j)      #this gives value of i and j instead of write that we access it by super class method from parent class
       self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

v2d=C2dVec(1,3)
v3d=C3dVec(1,9,7)
print(v2d)
print(v3d)