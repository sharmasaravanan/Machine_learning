import random as rm

import numpy as np

a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
m=np.reshape(a,[3,3])
i=1
userInput = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

def display(a):
    print ("   ---  ---   ---")
    print ('  | ' +'' +a[0][0]+ '  | ' +a[0][1]+ '  | ' +a[0][2]+'  | ' )
    print ("   ---  ---   ---")
    print ('  | ' +'' +a[1][0]+ '  | ' +a[1][1]+ '  | ' +a[1][2]+'  | ' )
    print ("   ---  ---   ---")
    print ('  | ' +'' +a[2][0]+ '  | ' +a[2][1]+ '  | ' +a[2][2]+'  | ' )
    print ("   ---  ---   ---")

def result(val):
    if val=='x':
        print ("Player 1 won the game...")
    else:
        print ("Player 2 won the game...")


def check(ele):
    if len(set(ele))==1:
        return True
    else:
        return False

def diag(m):
    d1=list(set([m[0][0],m[1][1],m[2][2]]))
    d2=list(set([m[0][2],m[1][1],m[2][0]]))
    if (len(d1)==1 and d1[0]!=' ')or (len(d2)==1 and d2[0]!=' '):
        return True
    else:
        return False


print("Tic-Tac-Toe")
while i <= 9:
    val='0'
    display(m)
    if i%2!=0:
        print ("Player 1 has to play..")
        val="x"
        cell = int(input("Enter the position : "))
    else:
        print ("Player 2 has to play...")
        val='o'
        cell = rm.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    r = userInput[cell][0]
    c = userInput[cell][1]    
    if m[r][c]==' ':
        m[r][c]=val
    else:
        print("Specified cell is already filled. Please select different cel")
        continue
    if check(m[r]) or check(m[:, c]):
        display(m)
        result(val)
        break
    #     if check(m[:, c]):
    #         display(m)
    #         result(val)
    #         break
    if (r,c) in [(0,0),(0,2),(1,1),(2,2),(2,0)]:
        if diag(m):
            display(m)
            result(val)
            break
    i+=1
