import os
import time
import glob
import mmap
import heapq
import pickle
from collections import Iterable



def flatten(items, ignore_types=(str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types):
			for i in flatten(x):
				yield i
			'''
			yield from flatten(x) /// 
			'''

		else:
			yield x


def test_flatten():
	items = [1, 2, [3, 4, [5, 6], 7], 8]
	for x in flatten(items):
		print(x)

'''As I read through the articles thourgh Gourmet's archives, I found articles from 1940, 1950 are generatlly more hearty then those 
  written in 2000 or 1990's. This may be caused by my inner biased "xiang wang" to the old times, movies show me gentalemen only live in that 
  period of time, and true gourmets would apprecise more to both the cooking skills, the prepartion hear and the taste instead of the outlooking
  or the luxuery of a restaurant.

  And my father's old saying can be applied here, he usually joked with me: Do you know how much ice cream was in the past? 50cents.
  With 1 yuan you could live for 1 week, now 1 yuan can barely cover a loli pop.
  So is in USA. When in old time, a decent meal cost $3 and a "really bargin" in a decent restaurant -- When I say decent, I mean the flavor and
  the waiters' service and the atomsphere, plus the decorations. When nowadays, baby you have to prepare your card or cash, $50 at least.

  I talk as if I live through those fancies times. But really, I just read the articles and books. I dream of those old times. Wish I can have a time machine
  that I can go back and see how, why and what if?

  Well, in reality, first I don't have a time machine, and even if I do, probably I would feel the same way the person in "an tu sheng"'s fair tale, the 
  judge travelled to the time he worshipped most and "xing yun de tao xie" and feel just lucky to be back.

  '''

def test_heapq():
	with open("sorted_file1", 'rt') as file1, \
	       open("sorted_file2", 'rt') as file2, \
	       open("merged_file", 'wt') as outf:

	       for line in heapq.merge(file1, file2):
	       	outf.write(line)


def sortDictValues1(adict):
	keys = adict.keys()
	keys.sort()
	return [adict[key] for key in keys]
	

def sortDictValue2(adict):
	keys = adict.keys()
	keys.sort()
	return map(adict.get, keys)

def testDict():
	dict1 = {3: "one", 2:"two", 1:"three"}
	print(sortDictValues1(dict1))
	print(sortDictValue2(dict1))
	#dict2 = {}

import os.path
def read_into_buffer(filename):
	buf = bytearray(os.path.getsize(filename))
	with open(filename, 'rb') as f:
		f.readinto(buf)
	return buf

with open('sample.bin', 'wb') as f:
	f.write(b'Hello World')




def os_path1():
	path = '/Users/fengjiaojiang/Downloads/clustering.pdf'
	print os.path.basename(path)
	print os.path.dirname(path)
	print os.path.join('tmp', 'logstash', os.path.basename(path))
	path = '~/Downloads/clustering.pdf'
	print os.path.expanduser(path)
	print os.path.splitext(path)



def os_path2():
	print os.path.isfile('/Users/fengjiaojiang/Downloads/clustering.pdf')
	print os.path.isdir('/Users/fengjiaojiang/Downloads/clustering.pdf')
	print os.path.islink('/Users/fengjiaojiang/Downloads/')
	print os.path.getsize('/Users/fengjiaojiang/Downloads/clustering.pdf')
	print time.ctime(os.path.getmtime('/Users/fengjiaojiang/Downloads/clustering.pdf'))
	#print os.path.realpath('/Users/fengjiaojiang/Downloads/clustering')
	pass

def os_path3():
	dirs = '/Users/fengjiaojiang/Downloads/'
	names = [name for name in os.listdir(dirs) 
	  if os.path.isfile(os.path.join(dirs, name))]
	print names
	pass


def os_path4():
	pyfiles = glob.glob('/Users/fengjiaojiang/Documents/workspace/Python Cookbook/*.py')
	name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) 
	         for name in pyfiles]
	for name, size, mtime in name_sz_date:
		print(name, size, mtime)

