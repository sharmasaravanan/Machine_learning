# array -> list, tuple, dict

# list
L = [] # creating empty list

l = ['apple','mango',1,2,'a','f',3.14]

print(L)
print(l)

print(len(l))  # to get the length of the list

# slice and dice
print(l[3])

print(l[3:])

print(l[:3])

print(l[3:6])

# list methods

name = input("Enter your name :")
L.append(name)
L.append('xyz')
print(L)

l.insert(2,'kiwi')
print(l)

del l[3]
l.remove('f')
L.pop()
print(l)
print(L)

l.reverse()
print(l)

# tuple
l = ('apple','mango',1,2,'a','f',3.14)
print(l)

