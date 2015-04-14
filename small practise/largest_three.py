def list_dec(lis, dec_type):
	return [dec_type(e) for e in lis]



def minimumfile(filepath, delimiter):
	f = open(filepath, 'r')
	line = next(f)
	lines = (line.strip('\n') for  line in f)
	
	res = [min(list_dec(line.split(delimiter), int)) for line in lines]
	res = ' '.join(str(r) for r in res)
	return res
	#return res


if __name__ == '__main__':
	print minimumfile('largest_three_three.txt', ' ')
