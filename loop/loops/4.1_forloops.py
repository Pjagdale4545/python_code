# for i in range(6):   #it will give 0 to 5
#     print(i)

# for i in range(2,6):  #it will give 2 to 6
#      print(i)

# for i in range(10,34,2):  #it will give 10 to 33 with escaping second number
#      print(i)

a=[2,3,4,'apple',6]
for i in range(len(a)):
    print(a[i])
    i+=1

for item in a:   #it has same result 
    print(item)