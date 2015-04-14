import palindrome
import outputs
from linearfunction import linearfunction
from binarysearch import solve_monotonic, binarysearch

def filefunc(filepath):
	f = open(filepath, 'r')
	next(f)
	return f

#TODO: make a read function?
#TODO: read function how to read heard
#TODO: read function how to define end of line
def test_palindromes(filepath, inputfunc, outputfunc):
	lines = (line.strip('\n') for line in filefunc(filepath))
	res = inputfunc(lines)
	res = ' '.join(outputfunc(r) for r in res)
	print (res)

def test_linearfunction(filepath, inputfunc, outputfunc):
	lines = (line.strip('\n') for line in filefunc(filepath))
	solus = (linearfunction(*line.split()) for line in lines)
	res = ' '.join("({} {})".format(ele[0], ele[1]) for ele in solus)
	print (res)

def test_binarysearch(filepath, inputfunc):
	lines = (line.strip('\n').split() for line in filefunc(filepath))
	solutions = (solve_monotonic(line.pop(), binarysearch, *line) for line in lines)
	res = ' '.join("{}".format(answer) for answer in solutions)
	print res


if __name__ == '__main__':
	#test_palindromes('TestData/palindrome.txt', None, None)
	#test_linearfunction('TestData/linear_func.txt', linearfunction, None)
	test_binarysearch('TestData/binarysearch.txt', solve_monotonic)
	
	
