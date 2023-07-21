import random
def game(comp,you):
    if(comp==you):
        return None
    if(comp=='s' and you=='w'):
        return True
    elif(comp=='w' and you=='s'):
        return True
    elif(comp=='g' and you=='w'):
        return True
    else:
        return False
print("comp return Snake(s) Water(w) Gun(g)")
randNo=random.randint(1,3)
if(randNo==1):
    comp= 's'
elif(randNo==2):
    comp= 'w'
elif(randNo==3):
    comp= 'g'
you= (input("You return Snake(s) Water(w) Gun(g)"))
a=game(comp,you)
print(f"comp choose {comp}")
print(f"You choose { you }")
if a==None:
    print("game is tie")
elif a:
    print("You win")
else:
    print("You Lose")