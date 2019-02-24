min<-0
max<-100
attempt<-0
print("Think any number between 0-100 and keep it with you, let me find out!!")
while (TRUE) {
    comp<-sample(min:max,1)
    print(sprintf("\nIsn't it %d ?",comp))
    user<-readline(prompt = "Enter the option \n a.high \n b.low \n c.Bingo \n")
    attempt<-attempt+1
    if (user=="low"||user=="b") {
        min<-comp+1
        next
    } else if (user=="high"||user=="a") {
        max<-comp-1
        next
    } else if (user=="bingo"||user=="c") {
        print(sprintf ("\nThe number is in your mind is %d and computer took %d attempts",comp,attempt))
        break
    } else {
        print ("\nPlease enter the valid option")
        break
}
}
