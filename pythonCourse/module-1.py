# assigning values to different variables
a = 5  # int
b = 3.14  # float
c = "apple"  # string
d = True  # bool

# displaying the content to the user
print(1234)
print('Hello world!!!')
print(a)
print(c)
print("------------------------------")

# displaying the datatypes of the variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("------------------------------")

# different variations in using print method
# hello apple
# hello 5
print("----Method-1----")
print("hello",c)
print("hello",a)

print("----Method-2----")
print("hello " + c)
print("hello "+ str(a))

print("----Method-3----")
print("hello {}".format(c))
print("hello {}".format(a))

print("------------------------------")

# I bought 3kgs of mango for 145.34Rs
f = "mango"
p = 143.34
w = 3

print("i bought",w,"kgs of",f,"for",p,"Rs")
print("i bought "+str(w)+"kgs of "+f+" for "+str(p)+"Rs")
print("i bought {}kgs of {} for {}Rs".format(w,f,p))
print("------------------------------")

# getting input from user
name = input("Enter your name : ")
mobile = int(input("Enter your mobile number : "))  # either use this way to change the datatype 
# mobile = int(mobile)  # or use this approach
print(name, "=>", type(name))
print(mobile, "=>", type(mobile))
print("------------------------------")
