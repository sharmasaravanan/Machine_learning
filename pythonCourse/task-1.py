"""
write a python program to do the following operations.

n = 5
output = 555+55+5
615

"""
n = '5'
output = int(n+n+n) + int(n+n) + int(n)
print(output)

n = '5'
output = int(n*3) + int(n*2) + int(n)
print(output)

n = 5
output = int(str(n)+str(n)+str(n)) +  int(str(n)+str(n)) + n
print(output)

"""
write a python program to calculate the area of the circle and rectangle by getting the corresponding input from the user.

"""

print("Area of Circle")
r = float(input("Enter the radius of the circle :"))
area = 3.14 * r * r
print("Area of the circle is {:.2f}".format(area))


print("Area of Rectangle")
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle:"))
output = 0.5 * l * b
print("Area of Rectangle is {:.2f}".format(output))
