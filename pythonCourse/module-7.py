# dict, for loop, library

# dict

l = ['apple','mango',1,2,'a','f',3.14]

d = {'a':"apple",'b':"ball",12:"dog",3.14:12312445,'l':l,'b':"bat"}

print(d)

print(d.keys())

print(d.values())

d['f'] = 'fish'

del d[3.14]

print(d)

name = input("enter your name: ")
number = input("enter your number : ")
details = {"name":name, "number":number}

print(details)

# for loop
for i in range(3):
    print("hello")

for i in range(6):
    print(i)

for i in range(3):
    num = int(input("Enter any number :"))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

name =  "elephant"
for i in name:
    print(i)
l = ['apple','mango',1,2,'a','f',3.14]

for i in l:
    print(i)

l = ['apple','mango',1,2,'a','f',3.14]

d = {'a':"apple",'b':"ball",12:"dog",3.14:12312445,'l':l,'b':"bat"}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,' --> ',v) 

# libraries

import math

ans = math.factorial(5)
print(ans)

print(math.pi)

import random as rd
print(rd.randint(1,10))

from math import factorial, pi, sin

print(factorial(5))
print(pi)
print(sin(10))

# to install -> pip install pandas
