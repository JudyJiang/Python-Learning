from collections import namedtuple

Point = namedtuple("Point", ["X", "Y"])
filter_type = lambda lis, type: (type(e) for e in lis)
linear_func = lambda x, y, a : y - a * x

def getA(point1, point2):
	try:
		a = (point1.Y - point2.Y) / (point1.X - point2.X)
		return a
	except ArithmeticError:
		if point1.Y == point2.Y:
			print ("Unlimitated Solution")
			exit(0)
		else:
			print ("No Solution")
			exit(1)

def linearfunction(*vals):
	try:
		tup = tuple(filter_type(vals, int))
	except TypeError:
		print ("Type Error, incompatable values {}".format(vals))
	try:
		point1 = Point(*tup[:2])
		point2 = Point(*tup[2:])
		a = getA(point1, point2)
		b = linear_func(point1.X, point1.Y, a)
		return (a,b)
	except IndexError:
		print ("Improper number of elements")
		exit(1)
