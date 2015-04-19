import math

PRECISION = 1e-7

filter_type = lambda lis, types: (types(e) for e in lis) if type(lis) is tuple else types(lis)
linear_func = lambda A, B: lambda x: A * x + B
sqrt_func = lambda A, B: lambda x: A * math.sqrt((math.pow(x, B)))
expontial = lambda A, B: lambda x: A * math.exp(B * x)
func = lambda A, B, C: lambda x: A*x + B * math.sqrt(math.pow(x, 3)) - C* math.exp(-0.02 * x)
#the test is the component function which is made up by small functions. It's not that direct but may appear more flexible to construct 
#functions with other parameters
test = lambda A1, B1, A2, B2, A3, B3: lambda x: linear_func(A1, B1)(x) + sqrt_func(A2, B2)(x) - expontial(A3, B3)(x)



def getright(func, initial, goal):
	while func(initial) < goal:
		initial *= 10
	return initial


def binarysearch(left ,right, func, goal, prec=PRECISION):
	count = 0
	if left is None:
		left = 0
	if right is None:
		right = getright(func, 10, goal)

	while left < right:
		mid = float(left + right) / float(2)
		res = func(mid)
		diff = abs(res - goal)
		if diff <= PRECISION:
			return mid
		else:
			if res > goal:
				right = mid
			else:
				left = mid

def binarysolver(goal, func):
	return binarysearch(None, None, func, goal)

def solve_monotonic(goal, method=binarysearch, *paras):
	try:
		goal = filter_type(goal, float)
		paras = tuple(filter_type(paras, float))
	except TypeError:
		print ("TypeError {}, {}".format(goal, *paras))
		exit(1)

	monotonic_func = func(*paras)
	return binarysolver(goal, monotonic_func)




