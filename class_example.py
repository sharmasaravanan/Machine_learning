'''
class Test:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def toJSON(self):
        	return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def test():
	t = Test('Dave', 'Kuhlman')
	print(t.toJSON())
	
test()


class B:
	def show(self,name):
		self.name=name
		print ('hello from ',self.name)
		

a=B()
a.show("sharma")


class B:
	def __init__(self,name):
		self.name=name
		
	def show(self):
		print ('hello from ',self.name)
		

a=B("sharma")
a.show()


class C:
	a=5
	def add(self,b):
		self.b=b
		print(C.a+self.b)
		

d=C()
d.add(15)


class A(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        print('name: %s' % (self.name,))


class B(A):
    def __init__(self, name, desc):
        A.__init__(self, name)
        self.desc = desc

    def show(self):
        A.show(self)
        print('desc: %s' % (self.desc,))


f = B("apple", "mango")
f.show()


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)



class Parent:

    def myMethod(self):
        print('Calling parent method')


class Child(Parent):
    def myMethod(self):
        print('Calling child method')


c = Child()
c.myMethod()
p = Parent()
p.myMethod()

# (10,20,10,40,50,60,70),50

# [-25, -10, -7, -3, 2, 4, 8, 10]

class D:
    def add(self,a,b,c=None):
        if c is None:
            print(a+b)
        else:
            print(a+b+c)

d=D()
d.add(5,8,10)

'''
