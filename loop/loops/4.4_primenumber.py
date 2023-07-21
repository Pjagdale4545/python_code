# num=int(input("enter the number"))
# prime=True
# if num==1:
#     prime=False
# if num >1:
#    for i in range(2,num):
#      if(num%i==0):
#         prime=False
#         break
# if prime:
#     print("prime number")
# else:
#     print("not prime")      



#sum of natural numbers------natural number start from 1
# i=1
# sum=0
# n=int(input("enter number to sum: "))
# while(i<=n):
#     sum+=i
#     i+=1
# print(f"sum of first {n} natural number is {sum}")


#-------------------factorial---------------3=3x2x1
# num=int(input("enter the number: "))
# factorial=1
# for i in range (1,num+1):
#    factorial=factorial*i
# print(f"factorial of {num} is {factorial} ")



#---------------pattern--------------

# for i in range(4):
#     print("*" * i)
#---------------------2---------------------------
# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#        print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     for j in range (n-i):
#         print(" ",end="") 
#     print("\n",end="")   


#-----------------------3-----------------
# n=int(input("enter the number: "))
# for i in range(n):
#     for j in range (n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#            print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n",end="")    



#------------------------------4--------------------------
num=int(input("enter the number: "))
for j in range(1,11):
    i = 11 - j
    print(f"{num}x{i}={num*i}")


