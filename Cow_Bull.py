import random as r
num=str(r.randint(100,999))
print (num)
j=0
while 1:
    user=input("Enter your guess: ")
    cowbull = [0,0]
    if user=="quit" or user=="q":
        print ("good bye..." )
        break  
    for i in range(len(num)):
        if num[i]==user[i]:
        	cowbull[0]+=1
    b=len(set(num)&set(user))
    cowbull[1]=b-cowbull[0]
    j+=1
    if cowbull[0]==3:
        print ("you win after",j,"attempts")
        break
    else:
        print("Your guess isn't quite right, try again.")
    print("Cow : %d and Bull : %d" % (cowbull[0], cowbull[1]))
