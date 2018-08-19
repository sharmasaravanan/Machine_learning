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

'''


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
