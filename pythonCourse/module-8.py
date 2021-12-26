# functions


# no arg no return
def operation():
    a = int(input("Enter any number :"))
    b = int(input("Enter any number :"))
    print(a+b, a*b)

operation()

# no arg with return
def operation():
    a = int(input("Enter any number :"))
    b = int(input("Enter any number :"))
    return a+b, a*b

s,m = operation()
print('sum is',s,', mul is',m)

s,m = operation()
print('sum is',s,', mul is',m)

s,m = operation()
print('sum is',s,', mul is',m)

# with arg with return
def operation(a,b):
    return a+b, a*b

a = int(input("Enter any number :"))
b = int(input("Enter any number :"))
s,m = operation(b,a)
print('sum is',s,', mul is',m)

s,m = operation(b,a)
print('sum is',s,', mul is',m)

s,m = operation(b,a)
print('sum is',s,', mul is',m)

# prime number check
def isPrimeCheck(num):
    for j in range(2, num):
        if num % j == 0:
            break
    else:
        return num
    
numbers = list(range(1,10))
print(numbers)

for i in numbers:
    ans = isPrimeCheck(i)
    if ans:
        print(ans)


# with default value
def operation(a,b=10):
    return a+b, a*b

a = int(input("Enter any number :"))
b = int(input("Enter any number :"))
s,m = operation(a)
s,m = operation(a,b)
print('sum is',s,', mul is',m)



add = lambda a,b,c : a+b+c
print(add(2,3,5))

upperCase = lambda string : string.upper()

print(upperCase('sharma'))




