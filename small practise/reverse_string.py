#reverse words within a string

def reverse_words(string, delimeter=None):
	try:
		if delimeter is None:
			words = string.split()
		else:
			words = string.split(delimeter)
		res = ' '.join(reversed(words))
		return res
	except TypeError:
		print ("Input String {}".format(string))


def run_test():
	test_lists = ['My name is Judy', ' This is nice ', "   How    Pretty", None]
	for case in test_lists:
		print (reverse_words(case))

if __name__ == '__main__':
	run_test()
