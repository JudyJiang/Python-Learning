from struct import Struct

def write_struct(records, format, f):
	record_struct = Struct(format)
	for r in records:
		f.write(record_struct.pack(*r))

def read_records(format, f):
	record_struct = Struct(format)
	#print record_struct.size record_struct.size is each line's data (array) size
	chunks = iter(lambda:f.read(record_struct.size), b'')
	return (record_struct.unpack(chunk) for chunk in chunks)



#encode data to binary array or uniform structure
def test_write_struct():
	records = [(1, 2.3, 4.5, 1.23), (6, 7.8, 9.0, 6.78), (12, 13.4, 56.7, 9.55)]
	with open('data.b', 'wb') as f:
		write_struct(records, '<iddd', f)

def test_read_struct():
	with open('data.b', 'rb') as f:
		#idd means pack (3) iddd means unpack "4"
		for rec in read_records('<iddd', f):
			print rec

def unpack_records(format, data):
	record_struct = Struct(format)
	return (record_struct.unpack_from(data, offset)
		for offset in range(0, len(data), record_struct.size))

def test_diff_size_unpack():
	pass

#test_write_struct()
#test_read_struct()


for i in range(0, 10, 3):
	print i