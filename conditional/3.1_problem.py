m1=int(input("enter the marks for sub1: "))
m2=int(input("enter the marks for sub2: "))
m3=int(input("enter the marks for sub3: "))

overall=((m1+m2+m3)/300)*100

if (overall>=40):
    if(m1>=33 and m2>=33 and m3>=33):
       print("you have passed exam")
    else:
       print("you are not passed the exam due to one of the subject")
else:
    print("you are not passed the exam due to overall percentage")