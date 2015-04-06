import palindrome
import outputs

#TODO: make a read function?
#TODO: read function how to read heard
#TODO: read function how to define end of line
def test_palindromes(filepath, inputfunc, outputfunc):
	f = open(filepath, 'r')
	next(f)
	lines = (line.strip('\n') for line in f)
	res = palindrome.if_palindorme(lines)
	res = ' '.join(outputs.replace_output(r) for r in res)
	print (res)


import datetime
print (type(datetime.datetime))

if __name__ == '__main__':
	test_palindromes('TestData/palindrome.txt', None, None)
	
	
