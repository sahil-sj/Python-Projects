import random
def checkwin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        else:
            return True
    elif comp=='w':
        if you=='s':
            return True
        else:
            return False
    elif comp=='g':
        if you=='w':
            return True
        else:
            return False
a=1
while(a):
    comp=random.randint(1,3)
    if comp==1:
        comp='s'
    elif comp==2:
        comp='g'
    else:
        comp='w'
    you=input("Your turn : snake(s), water(w), gun(g) : ")
    b=checkwin(comp,you)
    print(f"Computer chooses {comp} ")
    print(f"You chooses {you} ")
    if b==None:
        print("Game tie!")
    elif b==True:
        print("congratulations! You win")
    else:
        print("Computer wins! Sorry you lose")
    a=input("Enter q to exit and press any chracter to conitnue playing ")
    if(a=='q'):
        a=0
