#I'm ... the moment!
#. use a list or dict to store the fibonacci index and corresponding ValueError
#. before this, precompute 10 values. 
#. if the data is largest the largest one, keep adding and compute, store the staff in the dictionary. 
#. if small, just return the value-index.
#. the dictionary - datastructure is: 1. o(1) maximum value 2. order based on this
#. F value the "key", index the "value"

#because the lis got grown up!!!!
def fibonacci(N, lis):
	lis.append(0)
	lis.append(1)
	count = 1
	while count <= N:
		l = len(lis)
		tmp = lis[l-1] + lis[l-2]
		lis.append(tmp)
		count += 1

def fibonacciv(upvalue, lis):
	tmp = lis[len(lis) - 1] + lis[len(lis) -2]
	lis.append(tmp)
	while tmp < upvalue:
		tmp = lis[len(lis) - 1] + lis[len(lis) -2]
		lis.append(tmp)


def find_fibonacci_index(value):
	lis = []
	fibonacci(10, lis)
	if value < lis[len(lis) - 1]:
		return lis.index(value)
	else:
		fibonacciv(value, lis)
		return lis.index(value)


#498 452 678 350 122 926 386 646 694 944 351 25 718 80 56 798 160 612 225 233 196	

#498 452 678 350 122 926 386 646 694 944 351 25 718 80 56 798 160 612 225 233 196









