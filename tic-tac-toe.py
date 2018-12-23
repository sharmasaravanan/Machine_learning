import numpy as np
a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
m=np.reshape(a,[3,3])
i=1

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
		
while i<=9:
    print ("Tic-Tac-Toe")
    val='0'
    display(m)
    if i%2!=0:
        print ("Player 1 has to play..")
        val="x"
    else:
        print ("Player 2 has to play...")
        val='o'
    r = int(input("Enter the position e.g., 1,2 :"))
    if m[r][c]==' ':
        m[r][c]=val
    else:
        continue
    if check(m[r]):
        result(val)
        break
    if check(m[:, c]):
        result(val)
        break
    if (r,c) in [(0,0),(0,2),(1,1),(2,2),(2,0)]:
        if diag(m):
            result(val)
            break
    i+=1
