import palindrome
import outputs
from linearfunction import linearfunction
from binarysearch import solve_monotonic, binarysearch
from fibonacci_sequ import find_fibonacci_index

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

def test_fibonacci(filepath, inputfunc):
	lines = (line.strip('\n') for line in filefunc(filepath))
	solutions = (inputfunc(int(line)) for line in lines)
	res = ' '.join(str(ans) for ans in solutions)
	print res


if __name__ == '__main__':
	#test_palindromes('TestData/palindrome.txt', None, None)
	#test_linearfunction('TestData/linear_func.txt', linearfunction, None)
	#test_binarysearch('TestData/binarysearch.txt', solve_monotonic)
	test_fibonacci('TestData/fibonacci.txt', find_fibonacci_index)
	#498 452 678 350 122 926 386 646 694 944 351 25 718 80 56 798 160 612 225 233 196
	#498 452 1630 350 122 3031 386 1598 2799 5705 351 25 2823 80 56 2903 160 1564 225 233 196
