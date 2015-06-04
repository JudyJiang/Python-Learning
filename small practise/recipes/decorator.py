#http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#main point: make code cleaner, isolating the bounds checking!!!!
#finally I understand decorator a little bit


'''
so main point, decorator here is closure function (class?)
"outer" function takes function as parameters -> vars
"inner" function inside the outer function takes the parameters of vars (args)
make some decorations
so check vars' args, vars (a function) do something based on decorated or not decorated args
and return function 
''' 


#so decorator is closure function then descriptor is... class, generalized decorators
#so decorator is closure function then descriptor is... class, generalized decorators
#


def outer(some_func):
	def inner():
		print "some_func"
		ret = some_func()
		return ret + 1
	return inner

def foo():
	return "h"


def wrapper(func): # so maybe use * or ** dictionary based parameters
	def checker(a, b):
		if a.x < 0 or a.y < 0:
			a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
		if b.x < 0 or b.y < 0:
			b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
		ret = func(a, b)
		if ret.x < 0 or ret.y < 0:
			ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
		return ret 
	return checker


class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Coord: " + str(self.__dict__)

@wrapper #equals to add = wrapper(add), this is actually a closure
def add(a, b):
	return Coordinate(a.x + b.x, a.y + b.y)
@wrapper
def sub(a, b):
	return Coordinate(a.x, - b.x, a.y - b.y)


one = Coordinate(-1, 2)
two = Coordinate(3, -4)
#add = wrapper(add)
#sub = wrapper(add)

print add(one, two)