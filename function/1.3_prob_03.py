# if you dont want to print new line after the end of print statement use end="".....
# print("pooja and sachin",end="")
# print("and sheetal",end="####")

#write recursion function to sum of natural numbers

#sum(8)=1+2+3+4+5+6+7+8
#sum(n)=sum(n-1)+n

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
# a=sum(4)
# print(a)

#strip () is used to remove spaces
# a="    sachin is good    "
# print(a)
# print(a.strip())


#function for remove and replace
# def remove_strip(string, word):
#     newstr=string.replace(word,"")
#     return newstr.strip()
# a="  sachin is good  "
# n=remove_strip(a,"sachin")
# print(n)

#function for multiplication

def multi(num):
    num=int(input("enter the numbers: "))
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
a=multi()
print(a)  

#-----------------------second type-------------
def multi(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
a=multi(5)
print(a)

