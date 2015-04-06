import re
import string
#TODO1: is it necessary to put a 're' function here?
#TODO2: space and punctation staff...
exclude = set(string.punctuation)
def if_palindorme(input, case=False):
	for line in input:
		line = line if case else line.lower()
		line = re.sub('\s+', '', line)
		line = ''.join(ch for ch in line if ch not in exclude)
		reverse_line = ''.join(reversed(line))
		yield line == reverse_line

