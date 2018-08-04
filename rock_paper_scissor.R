user <- readline(prompt = "Enter your choice :")
comp <- readline(prompt = "Enter Comp's choice :")
if (user=="quit"||user=="q"){
     print ("Good Bye....")
     break
}
print(paste("Your choice is ",user,"and computer choice is ",comp))
if (user==comp){ 
    print("Game is tie")
    next
} else if (user=="rock") {
      if (comp=="scissor") {
          print ("user won the game")
       } else {
          print ("Computer won the game")
       }
} else if (user=="scissor") {
       if (comp=="paper") {
          print ("user won the game")
       } else {
          print ("computer won the game")
       }
} else if (user=="paper") {
        if (comp=="rock") {
          print ("user won the game")
        } else {
          print ("computer won the game")
        }
} else {
        print ("Have a nice day....!!!")
}

