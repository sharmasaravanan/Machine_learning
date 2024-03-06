min<-0
max<-100
attempt<-0
i<-0
while (i<1) {
  print("Think any number between 0-100 and keep it with you, let me find out!!")
  comp<-sample(min:max,1)
  print(sprintf("\nIsn't it %d ?",comp))
  user<-readline(prompt = "Enter the option \n a.high \n b.low \n c.Bingo \n")
  attempt<-attempt+1
  if (user=="low" | user=='a') {
    min<-comp+1
    next
  } else if (user=="high" | user=='b'){
    max<-comp-1
    next
  } else if (user=="bingo" | user=='c') {
    cat ("\nThe number is in your mind is", comp, "and computer took", attempt,"attempts")
    break
  } else {
    print ("\nPlease enter the valid option")
    break
  }
}
