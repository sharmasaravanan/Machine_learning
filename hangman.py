import random
print "Welcome to the game of HANGMAN!!!"
f=open("sowpods.txt",'r+')
lin=f.readlines()
words=[]
for i in lin:
    words.append(i.strip())
count=0
picked = random.choice(words)
print picked
print "The starting letter of word is ",picked[0]
ori=list(picked)
ans=list("_"*len(picked))
print ans
while 1:
    guess=str(raw_input("Enter your guess :"))
    count+=1   
    if guess.upper()in ori:
        num= [i for i, x in enumerate(ori) if x == guess.upper()]
        for x in num:
            ans[x]=guess.upper()
        print ans      
    else:
        continue
    if '_' not in ans:
        print "".join(ans)
        print "You won!!!, You have won the game in",count," attempts"
        break   
   
    
