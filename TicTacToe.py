def sum(a, b, c ):
    return a + b + c
def printboardd(x,y):
    a=  'X' if x[0] else ('O' if y[0] else 0)
    b=  'X' if x[1] else ('O' if y[1] else 1)
    c=  'X' if x[2] else ('O' if y[2] else 2)
    d=  'X' if x[3] else ('O' if y[3] else 3)
    e=  'X' if x[4] else ('O' if y[4] else 4)
    f=  'X' if x[5] else ('O' if y[5] else 5)
    g=  'X' if x[6] else ('O' if y[6] else 6)
    h=  'X' if x[7] else ('O' if y[7] else 7)
    i=  'X' if x[8] else ('O' if y[8] else 8)
    print(f"{a} | {b} | {c} ")
    print(f"{d} | {e} | {f} ")
    print(f"{g} | {h} | {i}  ")
def checkwin(x,y):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for wins in win:
        if(sum(x[wins[0]],x[wins[1]],x[wins[2]])==3):
            print("X Won the match")
            return 1
        if(sum(y[wins[0]], y[wins[1]], y[wins[2]]) == 3):
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("Welcome to Tic Tac Toe")
    while(True):
        printboardd(x,y)
        if(turn==1):
            print("X's chance : " )
            a=int(input("enter no where you want X : "))
            x[a]=1
            turn=turn-1
        else:
            print("0's chance: ")
            b=int(input("Enter no where you want O: "))
            y[b]=1
            turn=turn+1
        cwin=checkwin(x,y)
        if(cwin != -1):
            print("Match over")
            break
        
        

