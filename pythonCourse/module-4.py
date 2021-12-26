# while  loop
i = 1
while i <= 5:
    a = int(input("Enter any number for a: "))
    b = int(input("Enter any number for b: "))
    if a > b:
        print("A is greater than B")
    elif a == b:
        print("A is equal to B")
    else:
        print("A is lesser than B")
    i = i + 1


opt = 'y'
while opt == 'y':
    a = int(input("Enter any number for a: "))
    b = int(input("Enter any number for b: "))
    if a > b:
        print("A is greater than B")
    elif a == b:
        print("A is equal to B")
    else:
        print("A is lesser than B")
        
    opt = input("Do you want to continue? y/n :")

while True:
    a = int(input("Enter any number for a: "))
    b = int(input("Enter any number for b: "))

    if a == 15:
        print("Stopping....")
        break
    
    if a > b:
        print("A is greater than B")
    elif a == b:
        print("A is equal to B")
    else:
        print("A is lesser than B")


while True:
    a = int(input("Enter any number for a: "))
    b = int(input("Enter any number for b: "))
    if a > b:
        print("A is greater than B")
    elif a == b:
        print("A is equal to B")
    else:
        print("A is lesser than B")
        
    opt = input("Do you want to continue? y/n :")
    if opt == "n":
        print("Goodbye....")
        break
    elif opt == "y":
        continue
    else:
        print("please enter the valid option")
