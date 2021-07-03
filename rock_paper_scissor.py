j=["rock","scissor","paper"]
while 1:
    user = input("Enter your player-1 :")
    if user == "quit" or user == "q":
        print("Good Bye....")
        break
        
    comp = input("Enter your player-2 :")
    if comp == "quit" or comp == "q":
        print("Good Bye....")
        break
    print("player_1 choice is ", user, "and player_2 choice is ", comp)
    if user == comp:
        print("Game is tie")
        continue
    elif user == "rock":
        if comp == "scissor":
            print("user won the game")
        else:
            print("Computer won the game")
    elif user == "scissor":
        if comp=="paper":
            print ("user won the game")
        else:
            print ("computer won the game")
    elif user=="paper":
        if comp=="rock":
            print ("user won the game")
        else:
            print ("computer won the game")
    else:
        print ("Have a nice day....!!!")
