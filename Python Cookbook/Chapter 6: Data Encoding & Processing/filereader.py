import os
import re
import csv
from collections import namedtuple

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(DIR, 'data')
STOCK = os.path.join(DATA, 'stock.csv')


#this probably is the place to use decorator
def defaultprint(string=None):
	if string:
		print string

def defaultyield(obj=None):
	if obj:
		yield obj

#normal csv reading
def read_csv1(file, header=True, coltuple=None,func=defaultprint): #func can also be yield
	with open(file) as f:
		f_csv = csv.reader(f)
		if header:
			headers = [re.sub('[^a-zA-Z_]','_', h) for h in next(f_csv)]
			Row = namedtuple('Row', headers)
		for r in f_csv:
			if header:
				if coltuple:
					r = tuple(convert(value) for convert, value in zip(coltuple, r))
				row = Row(*r)
				func(string=row)
			else:
				func(string=row)


#use csv.Dictreader
#this automatically detect header
def read_csv2(file, header=None, func=defaultprint):
	with open(file) as f:
		csv_f = csv.DictReader(f)
		for row in csv_f:
			func(row)


def read_file(file, func=None):
	#TODO check the file appendix 
	#so as to make correct call
	pass


#read_csv1(STOCK, coltuple=[str, float, str, str, float, int])