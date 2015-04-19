def f(a, b):
	print a, b

def foo():
	func=f
	func(1, 2)


def test():
	foo()

#bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) for i in enumerate(mu)], key=lambda t:t[1])[0]
import numpy as np
X = np.random.random((4, 4))
g = np.linalg.norm

x = np.asarray([1, 2, 3])
i = np.asarray([3, 4, 5])

c1 = {}
c1[2] = [[2.3, 4.3], [4.7, 2.3]]
c1[0] = [[1.1, 2.2], [2.2, 3.3], [3.4, 5.3]]
c1[1] = [[3.3, 9], [3.9, 3.1]]

a = np.array([[1, 2], [1, 3], [2, 3], [4, 7]])
b = np.array([[1, 3], [1, 2], [2, 3], [4, 7]])

def foo(a, b):
	a1 = [tuple(i) for i in a]
	b1 = [tuple(i) for i in b]
	a1 = set(a1)
	b1 = set(b1)
	print a1
	print b1
	a1 = set(a)
	b1 = set(b)
	print a1==b1

foo(a, b)