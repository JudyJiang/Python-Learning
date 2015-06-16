import os
import sys
import math


if len(sys.argv) > 1:
	filename = sys.argv[1]
	if len(sys.argv) > 2: 
		funcname = sys.argv[2]
	else:
		funcname = 'pearson'
else:
	sys.exit("Missing input file\n")

	
x = []
y = []



def strip_value(line):
	buff = line.split()
	if len(buff) != 2:
		#ignore this line
		return 
	x.append(int(buff[0]))
	y.append(int(buff[1]))


def pearson(x, y):
	assert len(x) == len(y) > 0
	q = lambda n: len(n) * sum(map(lambda i: i ** 2, n)) - (sum(n)**2)
	rho = (len(x) * sum(map(lambda a: a[0] * a[1], zip(x, y))) - sum(x) * sum(y)) / math.sqrt(q(x) * q(y))
	print rho
	return rho


def spearman(x, y):
	pass #TODO: spearman algorithm

funcDict = {'pearson' : pearson}

def correlation():
	try:
		fname = filename
		func = funcname
		with open(fname) as f:
			map(strip_value, f.readlines())
		try:
			rho = funcDict[func](x, y)
			print rho
			print "final result: {rho}".format(rho=rho)
		except NameError:
			sys.exit("function not support")
	except ValueError:
		sys.exit("No Input File or Proper Function")



if __name__ == '__main__':
	correlation()