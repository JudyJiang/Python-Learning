import sys
from collections import Counter
from random import randint


def criteriaUsage():
	pass#TODO: function global

def funcA():
	value1 = 0

	def f(item, value):
		if item > 10:
			value += 1
		return value

	def setValue(item):
		nonlocal value1
		value1 = f(item, value1)

	def getValue():
		return value1

	f.setValue = setValue
	f.getValue = getValue
	return f #can decide return functions within closure based on parameters

def funcB():
	pass



def test():
	lis = [randint(0, 20) for i in range(5)]
	print (lis)

	fA = funcA()
	#fB = funcB()
	for item in lis:
		fA.setValue(item)
		#fB.setValue(item)
	print (fA.getValue())


def main():
	c1 = Counter({'dog':2, "cat":3, "bird":1})
	c2 = Counter({"dog":2, "cat":12, "bird":1})
	print (c1 + c2)
	


if __name__ == '__main__':
	sys.exit(main())